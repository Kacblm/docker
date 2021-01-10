from python

run pip install Flask uWSGI
workdir /app
copy app /app

#cmd ["python", "identidock.py"]

cmd ["uwsgi", "--http", "0.0.0.0:9090","--wsgi-file", "/app/identidock.py","--callable", "app", "--stats","0.0.0.0:9191"]
