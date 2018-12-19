from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
import sqlite3
from flask import g
import json
import re

app = Flask(__name__)

DATABASE = './test_demo_7.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/getData', methods=['GET', 'POST'])
def getData():
    cursor = get_db().cursor()
    cursor.execute( 'select * from COMPANY' )
    values = cursor.fetchall()
    print(values)
    print( type('runoob') )
    print( type( values ) )
    python2json = {}
    python2json["listData"] = values
    print( type( python2json ) )
    print( type( json.dumps(python2json)  ) )
    print( type( str(python2json)  ) )
    return json.dumps(python2json)


@app.route('/signup', methods=['GET'])
def signup_form():
    return '''<form action="/signup" method="post">
              <h6><input name="username"></h6>
              <h6><input name="password" type="password"></h6>
              <h6><button type="submit">Sign In</button></h6>
              </form>'''

@app.route('/signup', methods=['POST'])
def signup():
    res_username = re.match(r'^[0-9a-z]+$', request.form['username'])
    res_password = re.match(r'^[0-9a-z]+$', request.form['password'])
    if res_username and res_password:
        return '<h3>you are number</h3>'
    return '<h3>you are not number</h3>'

@app.route('/saveMoney', methods=['GET'])
def saveMoney_form():
    return '''<form action="/saveMoney" method="post">
              <h3>input money</h3>
              <h3><input name="saveMoney" ></h3>
              <h3><button type="submit">saveMoney</button></h3>
              </form>'''

@app.route('/saveMoney', methods=['POST'])
def saveMoney():
    print( request.form['saveMoney'] )
    saveMoney = re.match(r'^[0-9a-z]+$', request.form['saveMoney'])
    if saveMoney:
        return '<h3>saveMoney action success</h3>'
    return '<h3>saveMoney action error</h3>'

@app.route('/withdrawMoney', methods=['GET'])
def withdrawMoney_form():
    return '''<form action="/withdrawMoney" method="post">
              <h3>input withdrawMoney</h3>
              <h3><input name="withdrawMoney" ></h3>
              <h3><button type="submit">saveMoney</button></h3>
              </form>'''

@app.route('/withdrawMoney', methods=['POST'])
def withdrawMoney():
    print( request.form['withdrawMoney'] )
    withdrawMoney = re.match(r'^[0-9a-z]+$', request.form['withdrawMoney'])
    if withdrawMoney:
        return '<h3>withdrawMoney action success</h3>'
    return '<h3>withdrawMoney action error</h3>'

@app.route('/balanceQuery', methods=['GET'])
def balanceQuery_form():
    return '''<form action="/balanceQuery" method="post">
              <h1>input balanceQuery</h1>
              <h3>card number</h3>
              <h3><input name="card_number" ></h3>
              <h3>password</h3>
              <h3><input name="card_password" ></h3>
              <h3><button type="submit">submit</button></h3>
              </form>'''

@app.route('/balanceQuery', methods=['POST'])
def balanceQuery():
    print( 'card_number:',request.form['card_number'] )
    print( 'card_password:',request.form['card_password'] )
    card_number = re.match(r'^[0-9a-z]+$', request.form['card_number'])
    card_password = re.match(r'^[0-9a-z]+$', request.form['card_password'])
    if card_number:
        return '<h3>balanceQuery action success</h3>'
    return '<h3>balanceQuery action error</h3>'

@app.route('/openAnAccount', methods=['GET'])
def openAnAccount_form():
    return '''<form action="/openAnAccount" method="post">
              <h1>input openAnAccount</h1>
              <h3>user_name</h3>
              <h3><input name="user_name" ></h3>
              <h3>user_location</h3>
              <h3><input name="user_location" ></h3>
              <h3>user_birthdate</h3>
              <h3><input name="birthdate" ></h3>
              <h3>user_id</h3>
              <h3><input name="user_id" ></h3>
              <h3>user_phone</h3>
              <h3><input name="user_phone" ></h3>
              <h3><button type="submit">submit</button></h3>
              </form>'''

@app.route('/openAnAccount', methods=['POST'])
def openAnAccount():
    print( request.form['user_name'] )
    openAnAccount = re.match(r'^[0-9a-z]+$', request.form['user_name'])
    if openAnAccount:
        return '<h3>openAnAccount action success</h3>'
    return '<h3>openAnAccount action error</h3>'

if __name__ == '__main__':
    app.run()