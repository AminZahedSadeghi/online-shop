from django import template

register = template.Library()

@register.filter
def translate_number(value):
    persian = '۰۱۲۳۴۵۶۷۸۹'
    english = '0123456789' 
    
    value = str(value)
    engligh_to_persian_table = value.maketrans(english, persian)
    return value.translate(engligh_to_persian_table)