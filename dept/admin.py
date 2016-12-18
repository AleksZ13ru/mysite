from django.contrib import admin
from .models import People, Function, Holiday,\
    Schedule, Weekend, Change


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('fio', 'function', 'schedule')


class ChangeInline(admin.TabularInline):
    model = Change
    extra = 0


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'startday')
    inlines = [ChangeInline]


admin.site.register(Function)
admin.site.register(People, PeopleAdmin)
admin.site.register(Holiday)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Weekend)
