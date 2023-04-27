# -*- coding: utf-8 -*- 
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/chat')
def chat():
    user = {'username': 'Adam Jensen'}
    posts = [
        {
            'author': {'username': 'Jeff'},
            'body': 'My name is Jeff.'
        },
        {
            'author': {'username': 'Guard'},
            'body': 'I used to be an adventurer like you, then I took an arrow in the knee.'
        },
        {
            'author': {'username': 'Anon'},
            'body': 'sup guys, <$#fds> in the house!'
        },
        {
            'author': {'username': 'test_name'},
            'body': 'Sample text. Lorem ipsum.'
        }
    ]
    return render_template('chat.html', title='Home', user=user, posts=posts)