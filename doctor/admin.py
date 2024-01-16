from django.contrib import admin
from .models import AvailableTime,Specialization,Designation,Doctor,Review
# Register your models here.

admin.site.register(AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(Specialization, SpecializationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Designation, DesignationAdmin)

admin.site.register(Doctor)
admin.site.register(Review)
