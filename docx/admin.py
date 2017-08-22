from django.contrib import admin
from .models import Memo, PeopleToWhom, Event, Note


# Register your models here.
admin.site.register(Memo)
admin.site.register(PeopleToWhom)
admin.site.register(Event)
admin.site.register(Note)
