from django.contrib import admin
from .models import Memo, PeopleToWhom, PeopleWho, Event, Note


class EventInline(admin.TabularInline):
    model = Event
    extra = 0


class NoteInline(admin.TabularInline):
    model = Note
    extra = 0


class MemoAdmin(admin.ModelAdmin):
    # list_display = ('title', 'day_create')
    inlines = [NoteInline, EventInline]


class PeopleToWhomInline(admin.TabularInline):
    model = Memo
    extra = 0


class PeopleToWhomAdmin(admin.ModelAdmin):
    # list_display = ('title', 'day_create')
    inlines = [PeopleToWhomInline]


class PeopleWhoInline(admin.TabularInline):
    model = Memo
    extra = 0


class PeopleWhoAdmin(admin.ModelAdmin):
    # list_display = ('title', 'day_create')
    inlines = [PeopleWhoInline]


admin.site.register(Memo, MemoAdmin)
admin.site.register(PeopleToWhom, PeopleToWhomAdmin)
admin.site.register(PeopleWho, PeopleWhoAdmin)
admin.site.register(Event)
admin.site.register(Note)
