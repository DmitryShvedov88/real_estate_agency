from django.contrib import admin
from .models import Flat, Complaints, Owner


class FlatsInline(admin.TabularInline):
    '''FlatsInlineOwner'''

    model = Owner.flats.through
    raw_id_fields = ['owner']


class AuthorAdmin(admin.ModelAdmin):
    '''Admin search'''

    search_fields = [
        'town',
        'address',
        'owner'
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
        'has_balcony'
        )
    raw_id_fields = (
        'likes',
        )
    inlines = [FlatsInline]
    exclude = ['flats']


class ComplaintsAdmin(admin.ModelAdmin):
    '''Complaints veiw'''
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    '''Owner veiw'''
    list_display = ('name', 'phone', 'owner_pure_phone')
    raw_id_fields = ('flats')


admin.site.register(
    Flat,
    AuthorAdmin
    )

admin.site.register(
    Complaints,
    ComplaintsAdmin
    )

admin.site.register(
    Owner,
    OwnerAdmin
    )
