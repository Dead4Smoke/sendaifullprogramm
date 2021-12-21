from django import template
from django.template.defaultfilters import stringfilter
from base.models import Usersdate

register = template.Library()


@register.filter
@stringfilter
def region(value):
    a = 'Заполните данные'
    autodok = Usersdate.objects.filter(User=value).first()
    if autodok and autodok.region:
        return autodok.region
    else:
        return a  
register.filter('region', region)

@register.filter
@stringfilter
def vrp(value):
    a = 'Заполните данные'
    autodok = Usersdate.objects.filter(User=value).first()
    if autodok and autodok.vrp:
        return f'{autodok.vrp} млрд руб.'
    else:
        return a
register.filter('vrp', vrp)

@register.filter
@stringfilter
def people(value):
    a = 'Заполните данные'
    autodok = Usersdate.objects.filter(User=value).first()
    if autodok and autodok.people:
        return f'{autodok.people} чел.'
    else:
        return a
register.filter('people', people)