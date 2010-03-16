import datetime
from django.contrib import admin
from models import *

class CoffeeRoasterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
        'url',
        'status',
        'created',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeeBeanAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
        'roaster',
        'status',
        'created',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeeDrinkAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
        'status',
        'created',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }
    list_filter = ('status',)

class CoffeeDrinkSizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }

class CoffeePlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
        'address',
        'city',
        'state',
        'zip',
        'status',
        'created',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        'slug': ('name',)
    }

class CoffeePlaceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
        'status',
        'created',
    )
    list_filter = ('status',)
    prepopulated_fields = {
        'slug': ('name',)
    }

class CoffeeLogAdmin(admin.ModelAdmin):
    list_display = (
        'consumption',
        'user',
        'coffee_drink', 
        'coffee_drink_size',
        'coffee_place',
        'is_homemade',
        'coffee_bean',
        'status',
        'created',
    )
    ordering = ['-consumption']
    list_filter = list_display
    
    def get_form(self, request, obj=None, **kwargs):
        self.current_user = request.user
        return super(CoffeeLogAdmin, self).get_form(request, obj, **kwargs)
    
    def formfield_for_dbfield(self, field, **kwargs):
        from django import forms
        from django.contrib.auth.models import User
        
        if field.name == 'user':
            qs = User.objects.all()
            return forms.ModelChoiceField(queryset=qs, initial=self.current_user.id)
        
        return super(CoffeeLogAdmin, self).formfield_for_dbfield(field, **kwargs)

admin.site.register(CoffeeBean, CoffeeBeanAdmin)
admin.site.register(CoffeeDrink, CoffeeDrinkAdmin)
admin.site.register(CoffeeDrinkSize, CoffeeDrinkSizeAdmin)
admin.site.register(CoffeeLog, CoffeeLogAdmin)
admin.site.register(CoffeePlace, CoffeePlaceAdmin)
admin.site.register(CoffeePlaceCategory, CoffeePlaceCategoryAdmin)
admin.site.register(CoffeePlaceGeoPoint)
admin.site.register(CoffeeRoaster, CoffeeRoasterAdmin)
