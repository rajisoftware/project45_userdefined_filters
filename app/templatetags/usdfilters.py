from django import template 
register=template.Library()
@register.filter(name='swapping')
def swap(value):
    return value.swapcase()
#register.filter('swapping',swap)
@register.filter(name='replace')
def remove(value):
    return value.replace('H','')
#register.filter('replace',remove)
@register.filter(name='counting')
def  counting(value,arg):
    c=0
    for i in range(len(value)):
      if arg==value[i:i+len(arg)]:
        c+=1
    return c
#register.filter('counting',counting)