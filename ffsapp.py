# ffs: flask from scratch
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import sqlite3

# Create a DB if it doesnt exist and connect to itself.
connection = sqlite3.connect('db/ffs_db')

# Get a cursor to execute sql statements
cursor = connection.cursor()

# Create table users
sql = '''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
cursor.execute(sql)

# Insert data into table
# sql = "INSERT INTO users (name, email, usernme, password, register_date) VALUES ('str1', val1, etc)"
# cursor.execute(sql)

# Persist data
# connection.commit()

# Select data from table
# sql = 'SELECT * FROM users'
# cursor.execute(sql)

# rows = cursor.fetchall()

# for row in rows:
#    print(row)

# connection.close()

ffsapp = Flask(__name__)

Articles = Articles()


@ffsapp.route('/')
def index():
    # return 'Hallo Welt noch einmal!!!!'
    return render_template('home.html')


@ffsapp.route('/about')
def about():
    return render_template('about.html')


@ffsapp.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@ffsapp.route('/article/<string:id>/')
def article(id):
    # return render_template('articles.html', articles=Articles)
    # while we don't have sql ready, pass hardcoded id
    return render_template('article.html', id=id)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@ffsapp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)


# debug=True so that doesnt have to reinit server each time
if __name__ == '__main__':
    ffsapp.run(debug=True)
