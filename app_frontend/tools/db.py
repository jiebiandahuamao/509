#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: tools.py
@time: 16-1-25 下午8:39
"""

# todo get_rows order_by
# todo insert ignore


from app_frontend.database import db
from sqlalchemy.inspection import inspect


def get_row_by_id(model_name, pk_id):
    """
    通过 id 获取信息
    :param model_name:
    :param pk_id:
    :return: None/object
    """
    try:
        row = db.session.query(model_name).get(pk_id)
        db.session.commit()
        return row
    except Exception as e:
        db.session.rollback()
        raise e


def get_rows_by_ids(model_name, pk_ids):
    """
    通过一组 ids 获取信息列表
    :param model_name:
    :param pk_ids:
    :return: list
    """
    try:
        model_pk = inspect(model_name).primary_key[0]
        rows = db.session.query(model_name).filter(model_pk.in_(pk_ids)).all()
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def get_limit_rows_by_last_id(model_name, last_pk_id, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    适用场景：
    1、动态加载
    2、快速定位
    :param model_name:
    :param last_pk_id:
    :param limit_num:
    :param args:
    :param kwargs:
    :return: list
    """
    try:
        model_pk = inspect(model_name).primary_key[0]
        rows = db.session.query(model_name) \
                         .filter(model_pk > last_pk_id, *args) \
                         .filter_by(**kwargs) \
                         .limit(limit_num) \
                         .all()
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def get_row(model_name, *args, **kwargs):
    """
    获取信息
    Usage:
        # 方式一
        get_row(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_row(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/object
    """
    try:
        row = db.session.query(model_name).filter(*args).filter_by(**kwargs).first()
        db.session.commit()
        return row
    except Exception as e:
        db.session.rollback()
        raise e


def get_row_order_by_create_time_desc_first(model_name, *args, **kwargs):
    try:
        row = db.session.query(model_name) \
                        .filter(*args) \
                        .filter_by(**kwargs) \
                        .order_by(model_name.create_time.desc()) \
                        .first()
        db.session.commit()
        return row
    except Exception as e:
        db.session.rollback()
        raise e


def get_lists(model_name, *args, **kwargs):
    """
    获取列表信息
    Usage:
        # 方式一
        get_lists(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_lists(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/list
    """
    try:
        lists = db.session.query(model_name).filter(*args).filter_by(**kwargs).all()
        db.session.commit()
        return lists
    except Exception as e:
        db.session.rollback()
        raise e


def get_lists_info(model_name, model_out, Condition, *args, **kwargs):
    """
    获取列表信息
    Usage:
        # 方式一
        get_lists(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_lists(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/list
    """
    try:
        lists = db.session.query(model_name).outerjoin(model_out,Condition[0]).add_entity(model_out).filter(*args).filter_by(**kwargs).all()
        db.session.commit()
        return lists
    except Exception as e:
        db.session.rollback()
        raise e


def count(model_name, *args, **kwargs):
    """
    计数
    Usage:
        # 方式一
        count(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        count(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: 0/Number（int）
    """
    try:
        result_count = db.session.query(model_name).filter(*args).filter_by(**kwargs).count()
        db.session.commit()
        return result_count
    except Exception as e:
        db.session.rollback()
        raise e


def add(model_name, data):
    """
    添加信息
    :param model_name:
    :param data:
    :return: None/Value of model_obj.PK
    """
    model_obj = model_name(**data)
    try:
        db.session.add(model_obj)
        db.session.commit()
        return inspect(model_obj).identity[0]
    except Exception as e:
        db.session.rollback()
        raise e


def edit(model_name, pk_id, data):
    """
    修改信息
    :param model_name:
    :param pk_id:
    :param data:
    :return: Number of affected rows (Example: 0/1)
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk == pk_id)
        result = model_obj.update(data)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def increase(model_name, pk_id, field, num=1):
    """
    字段自增
    :param model_name:
    :param pk_id:
    :param field:
    :param num:
    :return: Number of affected rows (Example: 0/1)
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk == pk_id)
        value = getattr(model_name, field) + num
        data = {
            field: value
        }
        result = model_obj.update(data)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def merge(model_name, data):
    """
    覆盖信息(没有新增，存在更新)
    数据中必须带主键字段
    :param model_name:
    :param data:
    :return: Value of PK
    """
    model_obj = model_name(**data)
    try:
        r = db.session.merge(model_obj)
        db.session.commit()
        return inspect(r).identity[0]
    except Exception as e:
        db.session.rollback()
        raise e


def delete(model_name, pk_id):
    """
    删除信息
    :param model_name:
    :param pk_id:
    :return: Number of affected rows (Example: 0/1)
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk == pk_id)
        result = model_obj.delete()
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def get_rows(model_name, page=1, per_page=10, *args, **kwargs):
    """
    获取信息列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param model_name:
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return: None/object
    """
    try:
        rows = model_name.query. \
            filter(*args). \
            filter_by(**kwargs). \
            order_by(inspect(model_name).primary_key[0].desc()). \
            paginate(page, per_page, False)
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def insert_rows(model_name, data_list):
    """
    批量插入数据（遇到主键/唯一索引重复，忽略报错，继续执行下一条插入任务）
    注意：
    Warning: Duplicate entry
    警告有可能会提示：
    UnicodeEncodeError:
    'ascii' codec can't encode characters in position 17-20: ordinal not in range(128)
    处理：
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')

    sql 语句大小限制
    show VARIABLES like '%max_allowed_packet%';
    参考：http://dev.mysql.com/doc/refman/5.7/en/packet-too-large.html

    :param model_name:
    :param data_list:
    :return:
    """
    try:
        result = db.session.execute(model_name.__table__.insert().prefix_with('IGNORE'), data_list)
        db.session.commit()
        return result.rowcount
    except Exception as e:
        db.session.rollback()
        raise e


def update_rows(model_name, data, *args, **kwargs):
    """
    批量修改数据
    :param model_name:
    :param data:
    :param args:
    :param kwargs:
    :return:
    """
    try:
        model_obj = db.session.query(model_name).filter(*args).filter_by(**kwargs)
        result = model_obj.update(data, synchronize_session=False)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e


def update_rows_by_ids(model_name, pk_ids, data):
    """
    根据一组主键id 批量修改数据
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db.session.query(model_name).filter(model_pk.in_(pk_ids))
        result = model_obj.update(data, synchronize_session=False)
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        raise e

if __name__ == '__main__':
    pass