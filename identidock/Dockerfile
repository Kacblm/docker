from python

run groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
run pip install Flask uWSGI
workdir /app
copy app /app

EXPOSE 9090 9191
USER uwsgi
#cmd ["python", "identidock.py"]

cmd ["uwsgi", "--http", "0.0.0.0:9090","--wsgi-file", "/app/identidock.py","--callable", "app", "--stats","0.0.0.0:9191"]
