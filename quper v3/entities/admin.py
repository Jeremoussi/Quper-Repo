from django.contrib import admin
from . import models
# Register your models here.


# doest work yet
class EntityAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Entity._meta.get_fields()]
    list_display = ['entityName', 'user']




admin.site.register(models.Entity, EntityAdmin)
admin.site.register(models.Activity)
admin.site.register(models.ActivityGroup)
admin.site.register(models.Comment)
