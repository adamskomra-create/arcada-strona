#!/usr/bin/env bash
# Jednorazowe ustawienie automatu: serwer co 2 minuty pobiera stronę z GitHuba.
# Repozytorium jest publiczne, więc nie potrzeba żadnego klucza.
set -u
IP=169.58.235.17; U=root
REPO="https://github.com/adamskomra-create/arcada-strona.git"
echo "══════════════════════════════════════════════"
echo "  Arcada - ustawienie automatu pobierania"
echo "══════════════════════════════════════════════"
echo "Repozytorium: $REPO"
echo "Serwer:       $U@$IP"
echo
ssh -t -o StrictHostKeyChecking=accept-new "$U@$IP" "bash -s" <<'ZDALNE'
set -u
REPO="https://github.com/adamskomra-create/arcada-strona.git"
SRC=/opt/arcada-src

command -v git   >/dev/null || { apt-get update -qq && apt-get install -y -qq git; }
command -v rsync >/dev/null || apt-get install -y -qq rsync

if [ ! -d "$SRC/.git" ]; then
  rm -rf "$SRC"
  git clone --depth 1 "$REPO" "$SRC" || { echo "✗ Nie udało się sklonować $REPO"; exit 1; }
  echo "✓ Sklonowano repozytorium"
else
  echo "✓ Repozytorium już jest na serwerze"
fi

cat > /usr/local/bin/arcada-sync <<'SYNC'
#!/usr/bin/env bash
# Pobiera pliki strony z GitHuba i wgrywa TYLKO katalog www.
# Katalog demo celowo nietykany - jego treść żyje własnym życiem na serwerze.
set -u
SRC=/opt/arcada-src
DST=/opt/arcada
LOG=/var/log/arcada-sync.log
cd "$SRC" || exit 0
git fetch --depth 1 origin main -q 2>/dev/null || exit 0
NOWE=$(git rev-parse origin/main 2>/dev/null)
STARE=$(git rev-parse HEAD 2>/dev/null)
[ "$NOWE" = "$STARE" ] && exit 0
git reset --hard origin/main -q || exit 1
if [ -d "$SRC/www" ]; then
  # strona/ nalezy do panelu - on ja generuje z bazy, wiec nie nadpisujemy
  if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx arcada-panel; then
    rsync -a --delete --exclude 'strona/***' "$SRC/www/" "$DST/www/"
  else
    rsync -a --delete "$SRC/www/" "$DST/www/"
  fi
  echo "$(date '+%F %T')  wgrano ${NOWE:0:8}" >> "$LOG"
else
  echo "$(date '+%F %T')  POMINIETO: brak katalogu www w repozytorium" >> "$LOG"
fi
SYNC
chmod +x /usr/local/bin/arcada-sync

( crontab -l 2>/dev/null | grep -v arcada-sync; echo "*/2 * * * * /usr/local/bin/arcada-sync" ) | crontab -
echo "✓ Automat ustawiony: sprawdzanie co 2 minuty"
echo "  Podgląd:  tail -f /var/log/arcada-sync.log"
echo
/usr/local/bin/arcada-sync
echo "✓ Pierwsze pobranie wykonane"
echo
echo "Na serwerze leży teraz:"
ls -1 /opt/arcada/www
ZDALNE
echo
echo "Strona:  https://arcadaconcept.pl"
echo "Logo:    https://arcadaconcept.pl/logo"
echo "Serwis:  https://arcadaconcept.pl/strona"
echo
read -n1 -p "Enter zamyka okno..."
