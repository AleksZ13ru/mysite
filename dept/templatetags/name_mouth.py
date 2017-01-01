from django import template
import calendar
import datetime
from django.utils import timezone
register = template.Library()


@register.filter
def name_mouth(month_idx):
    td = timezone.now()
    td = td.replace(month=month_idx+1, day=1)
    return td
