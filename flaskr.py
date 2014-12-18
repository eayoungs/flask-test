import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# Config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# Application
app = flask(__name__)
app.config.from_object(__name__)
