from django.contrib import admin

from .models import Flat, Complain, Owner


class FlatInline(admin.TabularInline):
    model = Owner.owners_flats.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ("liked_by",)
    inlines = [FlatInline, ]


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat_id", 'author',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("owners_flats",)
    inlines = [FlatInline, ]
    exclude = ['owners_flats']


