import ast
from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.db import *


def get_one(pk):
    sql = "select user_id, first_name, last_name, user_name, phone from tg_tguser where user_id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None
        return result


def get_all(pk):
    sql = "select user_id, first_name, last_name, user_name, phone from tg_tguser"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dict_fetchall(cursor)
        result = []
        for i in data:
            result.append(_format(i))


def _format(data):
    return OrderedDict([
        ('user_id', data['user_id']),
        ('first_name', data['first_name']),
        ('last_name', data['last_name']),
        ('phone', data['phone']),
        ('user_name', data['user_name']),
    ])




