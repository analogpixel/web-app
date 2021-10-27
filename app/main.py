from flask import Flask, Blueprint, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    db_server = str( os.environ.get('db_server', default='no_value' ) )
    return render_template('index.html', db_server=db_server)

@app.route('/topic')
def get_topic():
    # https://kafka-python.readthedocs.io/en/master/usage.html
    print("topics")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

