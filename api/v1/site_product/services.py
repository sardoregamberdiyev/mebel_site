import ast
from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.db import *


def get_one(pk):
    sql = """ 
    select prod.id, prod."name", img.image, prod.price, prod.price_type, prod.color, prod.color, prod.short_description,
    prod."size",ctg."content", ctg.slug
    from sitee_product prod
    inner join sitee_category ctg on ctg.id = prod.ctg_id
    
    inner join(
    select s_i.product_id, array_to_json(array_agg(row_to_json(s_i))) as image 
    from sitee_productimage s_i
    group by s_i.product_id 
    ) img on img.product_id = prod.id
    where prod.id=%s
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None
        return result


def get_all():
    sql = """
        select prod.id, prod."name", img.image, prod.price, prod.price_type, prod.color, prod.color, prod.short_description,
        prod."size",ctg."content", ctg.slug
        from sitee_product prod
        inner join sitee_category ctg on ctg.id = prod.ctg_id
        
        inner join(
        select s_i.product_id, array_to_json(array_agg(row_to_json(s_i))) as image 
        from sitee_productimage s_i
        group by s_i.product_id 
        ) img on img.product_id = prod.id
        
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dict_fetchall(cursor)
        result = []
        for i in data:
            result.append(_format(i))

    return result


def _format(data):
    if data['image']:
        images = []
        for i in data['image']:
            images.append(i['image'])
    else:
        images = []

    if data['size']:
        size = ast.literal_eval(data['size'])
    else:
        size = None

    return OrderedDict([
        ('id', data['id']),
        ('name', data['name']),
        ('image', images),
        ('price', data['price']),
        ('color', data['color']),
        ('desc', data['short_description']),
        ('size', size),
        ('ctg', data['content']),
        ('slug', data['slug']),
    ])
