import time
from flask import Flask


app = Flask(__name__)


@app.route('/<uri>')
def foo(uri):
    time.sleep(1)
    return f'hello {uri}'


app.run()
