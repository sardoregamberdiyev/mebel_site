import ast
from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.db import *


def get_one(pk):
    sql = "select user_id, message from tg_log where user_id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None
        return result


def get_all(pk):
    sql = "select user_id, message from tg_log"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchall(cursor)
        result = []
        for i in data:
            result.append(_format(i))


def _format(data):
    if data['message']:
        message = ast.literal_eval(data['message'])
    else:
        message = None

    return OrderedDict([
        ('user_id', data['user_id']),
        ('message', message)
    ])













