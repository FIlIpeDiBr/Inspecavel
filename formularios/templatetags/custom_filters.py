from django import template
from django.forms import CheckboxInput, TextInput
from django.db.models import DateTimeField

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

@register.filter(name='add_label_class')
def add_label_class(field, css_class):
    return field.label_tag(attrs={'class': css_class})

@register.filter(name='is_datetime')
def is_datetime(field):
    return isinstance(field.field, DateTimeField)

@register.filter(name='is_text')
def is_text(field):
    return isinstance(field.field.widget, TextInput)

@register.filter(name='is_checkbox')
def is_checkbox(field):
    return isinstance(field.field.widget, CheckboxInput)