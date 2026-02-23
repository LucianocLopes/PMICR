from django.contrib import admin

from .models import State, City, Address


class AddressInline(admin.TabularInline):
    """
    Inline addresses registration.
    """
    model = Address
    extra = 1
    ordering = ('zip_code', 'city', 'street_name')


class CityInline(admin.TabularInline):
    """
    Inline cities registration.
    """
    model = City
    extra = 1
    min_num = 1
    max_num = 1
    ordering = ('state', 'name')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """
    Admin configuration for state model
    """
    list_display = ('name', 'abbreviation')
    search_fields = ('name', 'abbreviation')
    inlines = [CityInline]
    ordering = ('abbreviation',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Admin configuration for city model
    """
    list_display = ('name', 'state')
    search_fields = ('name',)
    list_filter = ('state',)
    inlines = [AddressInline]
    ordering = ('state', 'name')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin configuration for address model
    """
    list_display = ('street_suffix', 'street_name', 'neighborhood', 'zip_code', 'city')
    search_fields = ('street', 'neighborhood', 'zip_code')
    list_filter = ('city__state', 'city')
    ordering = ('zip_code','city', 'street_name')
