from django import template

register = template.Library()

@register.filter
def separate_each_3(price):
    price = str(price)
    b, a = divmod(len(price), 3)
    return ",".join(([price[:a]] if a else []) + [price[a+3*i:a+3*i+3] for i in range(b)])

@register.filter
def calc_price_with_qty(price, qty):
    return price * qty