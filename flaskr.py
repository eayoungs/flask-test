import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# Application
app = flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
