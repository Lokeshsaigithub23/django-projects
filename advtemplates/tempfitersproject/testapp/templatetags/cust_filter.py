from django import template
register=template.Library()
def frist_five_upper(value):
    result=value[:3].upper()
    return result

def first_n_upper(value,n):
    resut=value[:n].upper()
    return resut
register.filter('ffu',frist_five_upper)
register.filter('fnu',first_n_upper)    