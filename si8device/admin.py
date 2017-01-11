from django.contrib import admin
from si8device.models import Departament, Sector, Equipment, Register, PollResult


class PollResultAdmin(admin.ModelAdmin):
    list_filter = ['pollresult_register']


class PollResultInline(admin.StackedInline):
    model = PollResult
    extra = 1


class RegisterAdmin(admin.ModelAdmin):
    inlines = [PollResultInline]
    list_filter = ['register_name', 'register_enable']


class RegisterInline(admin.StackedInline):
    model = Register
    extra = 1


class EquipmentAdmin(admin.ModelAdmin):
    inlines = [RegisterInline]
    list_filter = ['equipment_enable']


class EquipmentInline(admin.StackedInline):
    model = Equipment
    extra = 1


class SectorAdmin(admin.ModelAdmin):
    inlines = [EquipmentInline]


class SectorInline(admin.StackedInline):
    model = Sector
    extra = 1


class DepartamentAdmin(admin.ModelAdmin):
    inlines = [SectorInline]


class DepartamentInline(admin.StackedInline):
    model = [Departament]
    extra = 1


admin.site.register(PollResult, PollResultAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Departament, DepartamentAdmin)
