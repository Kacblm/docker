from python

run groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
run pip install Flask uWSGI requests redis
workdir /app
copy app /app
copy cmd.sh /

EXPOSE 9090 9191
USER uwsgi
#cmd ["python", "identidock.py"]
cmd ["/cmd.sh"]
#cmd ["uwsgi", "--http", "0.0.0.0:9090","--wsgi-file", "/app/identidock.py","--callable", "app", "--stats","0.0.0.0:9191"]
