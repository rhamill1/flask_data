from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'
    # return render_template('main.html')