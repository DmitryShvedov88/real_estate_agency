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

admin.site.register(
    Flat,
    AuthorAdmin,
    )
