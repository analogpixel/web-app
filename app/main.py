from flask import Flask, Blueprint, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    db_server = str( os.environ.get('db_server', default='no_value' ) )
    sql_query = str( os.environ.get('sql_query', default='select * from data' ) )

    if db_server != 'no_value':
        conn = psycopg2.connect(dbname="db", user="root", password="password", host=db_server)
        cur = conn.cursor()
        cur.execute(sql_query)
        v = ",".join([ x[1] for x in cur.fetchall() ])
    else:
        v = "no values"

    return render_template('index.html', db_server=db_server, v=v)

@app.route('/topic')
def get_topic():
    # https://kafka-python.readthedocs.io/en/master/usage.html
    print("topics")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

