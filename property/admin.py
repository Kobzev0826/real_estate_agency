from django.contrib import admin

from .models import Flat, Complain, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price','owners_phonenumber' ,'owner_pure_phone','new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ("liked_by",)


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat_id", 'author',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("owners_flats",)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
