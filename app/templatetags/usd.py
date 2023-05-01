from django import template

register=template.Library()

@register.filter(name='swap')
def swap(value):
    return value.swapcase()

@register.filter()
def count(value,arg ):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c

@register.filter()
def  remove(value,arg):
    return value.replace(arg,'')

#register.filter('count',count)
#register.filter('remove',remove)
#register.filter('swap',swap)