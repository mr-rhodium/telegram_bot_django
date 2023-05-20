from django.contrib import admin
from django.contrib.admin import ModelAdmin


from core.models import TUser


@admin.register(TUser)
class CoreAdmin(ModelAdmin):
    pass