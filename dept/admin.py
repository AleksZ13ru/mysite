from django.contrib import admin
from .models import People, Function, Holiday, Schedule, Weekend, Change


admin.site.register(Function)
admin.site.register(People)
admin.site.register(Holiday)
admin.site.register(Change)
admin.site.register(Schedule)
admin.site.register(Weekend)
