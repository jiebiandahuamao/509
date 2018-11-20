#-*- coding:utf8 -*-
def get_env():
    """
    获取运行环境
    """
    import os
    file_name = '/'.join((os.path.dirname(os.path.abspath(__file__)), 'config.env'))
    with open(file_name) as f:
        env = f.read()
        if env:
            return env.strip()
        else:
            return ''


config_env = get_env()
if config_env == 'product':
    from config.product import *
elif config_env == 'develop':
    from config.develop import *
elif config_env == 'locals':
    from config.local import *
else:
    from config.develop import *