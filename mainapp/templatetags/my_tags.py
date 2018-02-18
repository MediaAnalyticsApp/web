from django import template

register = template.Library()


@register.filter(name='up')
def up(st):
    return st.upper()


@register.filter(name='add_name')
def add_name(st, arg):
    return '{}: {}'.format(arg, st)


@register.simple_tag
# @register.filter(name='query_update')
def query_update(query, key, value):
    query = query.copy()
    query[key] = value
    return query.urlencode()
