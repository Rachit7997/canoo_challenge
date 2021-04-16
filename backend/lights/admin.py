from django.contrib import admin

from .models import Light

@admin.register(Light)
class lightAdmin(admin.ModelAdmin):
    pass
