#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: database.py
@time: 16-1-16 下午11:44
"""

import redis
from flask_sqlalchemy import SQLAlchemy
from app_frontend import app
db = SQLAlchemy(app)

redis_client = redis.Redis(**app.config['REDIS'])
