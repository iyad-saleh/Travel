from django.contrib import admin
from .models import Box

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ( 'id',
                'account',
                'company',
                'create_at',
                'author',
                )
    list_filter = (
                'company',
                'author',
                )
