#-*- coding:utf8 -*-
from flask import Flask
# import config
app = Flask(__name__)
app.config.from_object('config')


# 导入视图（不使用蓝图的单模式方式）
from app_frontend import views

#注册蓝图等
from app_frontend.views.login import bp_auth

# 注册蓝图
app.register_blueprint(bp_auth)



# 导入自定义过滤器
from app_frontend import filters



#各类插件接口

