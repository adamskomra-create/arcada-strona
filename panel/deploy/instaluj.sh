#!/usr/bin/env bash
# Instalacja panelu Arcada obok istniejacego kontenera ze strona.
set -euo pipefail
APP=/opt/arcada-src
DANE=/opt/arcada-panel/dane
WWW=/opt/arcada/www
ok(){ printf '\033[32m✓\033[0m %s\n' "$*"; }
die(){ printf '\033[31m✗ %s\033[0m\n' "$*"; exit 1; }

[ -d "$APP/panel" ] || die "Nie widzę $APP/panel - najpierw musi zadziałać arcada-sync"
mkdir -p "$DANE/zdjecia" "$WWW/strona"

CADDY=$(docker ps --filter publish=443 --format '{{.Names}}' | grep -E 'caddy' | head -1 || true)
[ -n "$CADDY" ] || die "Nie widzę kontenera Caddy"
NET=$(docker inspect "$CADDY" --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}}' | tr ' ' '\n' | grep -m1 .)
ok "Caddy: $CADDY, sieć: $NET"

cd "$APP/panel"
docker build -q -t arcada-panel:latest -f deploy/Dockerfile . >/dev/null
ok "Obraz zbudowany"

SEKRET=$(cat /opt/arcada-panel/.sekret 2>/dev/null || { openssl rand -hex 32 | tee /opt/arcada-panel/.sekret; })
chmod 600 /opt/arcada-panel/.sekret

docker rm -f arcada-panel >/dev/null 2>&1 || true
docker run -d --name arcada-panel --restart unless-stopped --network "$NET" \
  -e ARCADA_SECRET="$SEKRET" \
  -v "$DANE:/dane" \
  -v "$WWW/strona:/wynik/strona" \
  arcada-panel:latest >/dev/null
sleep 4
docker exec arcada-panel python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8080/zdrowie').read()" \
  && ok "Panel działa" || die "Panel nie odpowiada: docker logs arcada-panel"

SRC=$(docker inspect "$CADDY" --format '{{range .Mounts}}{{if eq .Destination "/etc/caddy/Caddyfile"}}{{.Source}}{{end}}{{end}}')
[ -n "$SRC" ] && [ -f "$SRC" ] || die "Nie znalazłem Caddyfile"
if grep -q "handle /panel" "$SRC"; then
  ok "Wpis panelu już jest w Caddy"
else
  cp "$SRC" "$SRC.bak-panel-$(date +%Y%m%d%H%M%S)"
  python3 - "$SRC" <<'PY'
import re,sys
p=sys.argv[1]; t=open(p).read()
blok='''	handle /panel* {
		reverse_proxy arcada-panel:8080
	}
'''
t=re.sub(r'(arcadaconcept\.pl \{\n)', r'\1'+blok, t, count=1)
open(p,'w').write(t)
PY
  docker exec "$CADDY" caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile >/dev/null 2>&1 \
    || die "Caddy nie przyjął konfiguracji - przywróć kopię $SRC.bak-panel-*"
  docker exec "$CADDY" caddy reload --config /etc/caddy/Caddyfile --adapter caddyfile >/dev/null 2>&1 || docker restart "$CADDY" >/dev/null
  ok "Panel dodany do Caddy"
fi

echo
echo "Panel:  https://arcadaconcept.pl/panel"
echo "Przy pierwszym wejściu ustawisz hasło (min. 8 znaków)."
echo "Baza i zdjęcia: $DANE  (poza obrazem, przetrwają aktualizacje)"
