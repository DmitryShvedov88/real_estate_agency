from django.contrib import admin
from .models import Flat


class AuthorAdmin(admin.ModelAdmin):
    '''Admin search'''

    search_fields = [
        'town',
        'address',
        'owner',
        ]

    readonly_fields = [
        "created_at"
        ]
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year'
        )
    list_editable = ['new_building']
    # list_filter = (
    #     'address',
    #     'price',
    #     'construction_year'
    #     )
  
admin.site.register(
    Flat,
    AuthorAdmin,
    )
