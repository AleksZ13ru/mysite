from django.contrib import admin
from .models import People, Function, Holiday, \
    Schedule, Weekend, Change, MicroSchedule


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('fio', 'function', 'schedule')


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('people', 'year', 'typ', 'startday')


class ChangeInline(admin.TabularInline):
    model = Change
    extra = 0


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'startday',)
    inlines = [ChangeInline]


class MicroScheduleAdmin(admin.ModelAdmin):
    list_display = ('people', 'schedule', 'startday', 'lenght')


admin.site.register(Function)
admin.site.register(People, PeopleAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Weekend)
admin.site.register(MicroSchedule, MicroScheduleAdmin)
