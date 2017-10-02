from django.contrib import admin
from .models import Memo
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Memo, SimpleHistoryAdmin)
