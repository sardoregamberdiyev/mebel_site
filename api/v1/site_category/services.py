from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.db import *


def get_one(pk):
    sql = "select id, content, slug, icon, from sitee_category where id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None
        return result


def get_all(pk):
    sql = "select id, content, slug, icon, from sitee_category"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchall(cursor)
        result = []
        for i in data:
            result.append(_format(i))


def _format(data):
    return OrderedDict([
        ('id', data['id']),
        ('content', data['content']),
        ('slug', data['slug']),
        ('icon', data['icon']),
    ])
