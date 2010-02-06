import datetime
from django.contrib import admin
from models import *

class CoffeeRoasterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'url',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeeBeanAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'roaster',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeeDrinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeeDrinkSizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeePlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'address',
        'city',
        'state',
        'zip',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeePlaceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'created',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeeLogAdmin(admin.ModelAdmin):
    list_display = (
        'coffee_drink', 
        'coffee_drink_size',
        'coffee_place',
        'coffee_bean',
        'consumption',
    )
    ordering = ['-consumption']
    list_filter = list_display

admin.site.register(CoffeeBean, CoffeeBeanAdmin)
admin.site.register(CoffeeDrink, CoffeeDrinkAdmin)
admin.site.register(CoffeeDrinkSize, CoffeeDrinkSizeAdmin)
admin.site.register(CoffeeLog, CoffeeLogAdmin)
admin.site.register(CoffeePlace, CoffeePlaceAdmin)
admin.site.register(CoffeePlaceCategory, CoffeePlaceCategoryAdmin)
admin.site.register(CoffeePlaceGeoPoint)
admin.site.register(CoffeeRoaster, CoffeeRoasterAdmin)
