from django.contrib import admin
from .models import Flat, Complaints, Owner


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
    list_editable = [
        'new_building'
        ]
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
        )
    raw_id_fields = (
        'likes',
        )

class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'owner_pure_phone')
    raw_id_fields = ('flats',)

admin.site.register(
    Flat,
    AuthorAdmin,
    )

admin.site.register(
    Complaints,
    ComplaintsAdmin,
    )

admin.site.register(
    Owner,
    OwnerAdmin,
    )
