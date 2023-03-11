from django import template
from config.settings import LANGUAGE_CODE

register = template.Library()

@register.filter
def translate_number(value):
    value = str(value)
    
    persian = '۰۱۲۳۴۵۶۷۸۹'
    english = '0123456789' 

    if LANGUAGE_CODE == 'fa-ir':
        engligh_to_persian_table = value.maketrans(english, persian)
        return value.translate(engligh_to_persian_table)
    
    elif LANGUAGE_CODE == 'en-us':
        return value