from django.contrib import admin

from .models import Flat, Complain, Owner


class FlatInline(admin.TabularInline):
    model = Owner.owners_flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ("liked_by",)
    inlines = [FlatInline, ]


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat_id", 'author',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("owners_flats",)
    inlines = [FlatInline, ]
    exclude = ['owners_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
