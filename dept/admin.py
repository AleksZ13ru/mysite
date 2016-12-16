from django.contrib import admin
from .models import People, Function, Holiday


admin.site.register(Function)
admin.site.register(People)
admin.site.register(Holiday)
