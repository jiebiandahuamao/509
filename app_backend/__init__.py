#-*-coding:utf8 -*-
from flask import Flask

app = Flask(__name__)

app.config.from_object('config')


# 导入视图（不使用蓝图的单模式方式）
from app_backend import views

#注册蓝图等
from app_backend.views.index import bp_index

# 注册蓝图
app.register_blueprint(bp_index)



# 导入自定义过滤器
from app_backend import filters



#各类插件接口