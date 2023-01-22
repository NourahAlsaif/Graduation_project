from flask import Flask, session , request, render_template ,url_for , redirect
from flask import MYSQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key= 'xyzdsfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config ['MYSQL_DB'] = 'user-system'

mysql = MYSQL(app)


@app.route('/')
@app.route('/login', methods=['GET' , 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MYSQL.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email= % s AND password = % s', (email, password))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['email'] = user['email']
            session['password'] = user['password']
            mesage = 'Logged in successfuly!'
            return render_template('Login page.html', mesage=mesage)
        else:
            mesage = 'Please enter correct email/ password!'
            return render_template('Login page.html', mesage=mesage)

@app.route('/logout')
def logout():
    session.pop('Loggedin' , None)
    session.pop('email', None)
    return redirect(url_for(login))

@app.route('/signup', methods=['GET' , 'POST'])
def signup():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'fname' in request.form and 'lname' in request.form and 'password' in request.form:
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form['password']
        cursor = mysql.connection.cursor(MYSQL.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email= % s AND fname = % s AND lname = %s AND password = % s', (email, fname, lname, password))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists'
            return render_template('SignupPage.html', mesage=mesage)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email exists !'
            return render_template('SignupPage.html', mesage=mesage)
        elif not email or not fname or not lname or not password:
            mesage= 'Please fill out the form !'
            return render_template('SignupPage.html', mesage=mesage)
        else:
            cursor.execute('INSERT INTO user VALUES (NULL,% s,% s ,% s, %s)', (email,fname,lname,password , ))
            mysql.connection.commit()
            mesage ='You have successfuly sign up'
            return render_template('SignupPage.html', mesage=mesage)
    elif request.method=='POST':
        mesage = 'please fill out the form!'
        return render_template('SignupPage.html', mesage=mesage)

if __name__ == "__main__":
    app.run()

