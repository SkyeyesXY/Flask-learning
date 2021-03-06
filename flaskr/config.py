# -*- coding: utf-8 -*-
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/home/skyeyes/PycharmProjects/flaskr/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'skyeyes'    #admin
PASSWORD = '960524'     #default


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

