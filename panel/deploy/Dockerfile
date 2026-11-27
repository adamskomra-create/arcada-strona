FROM python:3.12-slim

RUN apt-get update -qq && apt-get install -y -qq --no-install-recommends \
      libwebp7 libjpeg62-turbo zlib1g \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask==3.0.3 gunicorn==22.0.0 pillow==10.4.0 bcrypt==4.2.0

WORKDIR /app
COPY app/    /app/app/
COPY strona/ /app/strona/

# baza i zdjecia zyja w wolumenie, nie w obrazie
ENV ARCADA_DB=/dane/arcada.db \
    ARCADA_ZDJECIA=/dane/zdjecia \
    ARCADA_STRONA=/app/strona \
    ARCADA_WYNIK=/wynik \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/app

RUN mkdir -p /dane /wynik
VOLUME ["/dane"]
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=4s --start-period=10s \
  CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8080/zdrowie').read()" || exit 1

CMD ["gunicorn","--chdir","/app/app","--bind","0.0.0.0:8080","--workers","2","--threads","4","--timeout","120","panel:app"]
