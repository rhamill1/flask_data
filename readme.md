##### Environment start up instructions
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install Flask
$ pip install gunicorn
$ pip install pandas
$ pip install scikit-learn
$ pip install scipy
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
##### Execute Data Science Scripts
```
$ venv/bin/python scripts/myers_briggs_text.py
```
