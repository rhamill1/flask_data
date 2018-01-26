##### Environment start up instructions
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install Flask
$ pip install gunicorn
$ pip freeze > requirements.txt
```
##### Deactivate Virtualenv
```
deactivate
```
##### Run Dev Server
```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ python -m flask run
```
##### Deploy to Heroku
```

```
