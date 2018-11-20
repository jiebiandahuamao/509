#-*- coding:utf8 -*-
from flask import render_template, request, redirect, flash, json
from app_frontend import app

@app.route('/')
def index():

    return "这是首页！！！"
