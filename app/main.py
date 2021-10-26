from flask import Flask, Blueprint
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return "hello World:" + str(os.environ.get('app_config_1'))
    return app.send_static_file('index.html')

@app.route('/topic')
def get_topic():
    # https://kafka-python.readthedocs.io/en/master/usage.html
    print("topics")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

