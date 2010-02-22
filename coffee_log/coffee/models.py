from django.db import models
from django.utils.text import force_unicode
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models
from coffee_log.settings_site import STATUS_OPTIONS
import djangosphinx

# Coffee Roasters

class CoffeeRoaster(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Roasters'
    
    @models.permalink
    def get_absolute_url(self):
        return ('coffee_log.coffee.views.roaster', [str(self.slug)])

# Coffee Beans

class CoffeeBean(models.Model):
    roaster = models.ForeignKey(CoffeeRoaster, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    type = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    search = djangosphinx.SphinxSearch('coffee_coffeebean')
    
    def __unicode__(self):
        return '%s (%s)' % (self.name, self.roaster.name)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Beans'
    
    @models.permalink
    def get_absolute_url(self):
        return ('coffee_log.coffee.views.bean', [str(self.slug)])

# Coffee Drinks

class CoffeeDrink(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return force_unicode(self.name)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Drinks'

# Coffee Drink Sizes

class CoffeeDrinkSize(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Drink Sizes'

# Coffee Place Category

class CoffeePlaceCategory(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Place Categories'

# Coffee Places

class CoffeePlace(models.Model):
    
    roaster = models.ForeignKey(CoffeeRoaster, blank=True, null=True)
    coffee_place_categories = models.ManyToManyField(CoffeePlaceCategory, blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('coffee_log.coffee.views.place', [str(self.slug)])
    
    def get_full_address(self):
        full_address = ''
        if self.address:
            full_address = self.address
        if self.city:
            full_address += ', ' + self.city
        if self.state:
            full_address += ', ' + self.state
        if self.zip:
            full_address += ' ' + str(self.zip)
        return full_address
    
    full_address = property(get_full_address)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Places'

# Coffee Place Geo Point

class CoffeePlaceGeoPoint(models.Model):
    coffee_place = models.OneToOneField(CoffeePlace)
    geo_address = models.CharField(max_length=255)
    geo_point = geo_models.PointField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = geo_models.GeoManager()

    class Meta:
        verbose_name_plural = 'Coffee Place Geo Points'

# Post save for CoffeePlace to create or update geo point

def create_coffee_place_geo_point(sender, instance, signal, *args, **kwargs):
    # out = ''
    # if not instance.address == '':
    #     from coffee_log.google_maps import get_geo_point
    #     print 'SEARCHING ADDRESS: ' + instance.full_address
    #     geo_point = get_geo_point(instance.full_address)
    #     if geo_point:
    #         out = 'FOUND'
    #         coffee_place_geo = ''
    #         try:
    #             coffee_place_geo = CoffeePlaceGeoPoint.objects.get(coffee_place=instance.pk)
    #         except:
    #             pass
    #         if coffee_place_geo:
    #             out += ', UPDATING GEO POINT'
    #             coffee_place_geo.geo_address = geo_point[0]
    #             coffee_place_geo.geo_point = geo_point[1]
    #         else:
    #             out += ', ADDING GEO POINT'
    #             coffee_place_geo = CoffeePlaceGeoPoint(coffee_place=instance, geo_address = geo_point[0], geo_point=geo_point[1])
    #         coffee_place_geo.save()
    #     else:
    #         out = 'NOT FOUND'
    # else:
    #     out = 'ADDRESS EMPTY'
    # print out
    return True

# Register CoffeePlace post save signal

models.signals.post_save.connect(create_coffee_place_geo_point, sender=CoffeePlace)

# Coffee Logs

class CoffeeLog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    coffee_drink = models.ForeignKey(CoffeeDrink)
    coffee_bean = models.ForeignKey(CoffeeBean, blank=True, null=True)
    coffee_place = models.ForeignKey(CoffeePlace, blank=True, null=True)
    coffee_drink_size = models.ForeignKey(CoffeeDrinkSize, blank=True, null=True)
    is_homemade = models.BooleanField(default=False)
    notes = models.CharField(max_length=255, blank=True, null=True)
    consumption = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS_OPTIONS, default=2)
    
    def __unicode__(self):
        display = ''
        if self.coffee_drink_size:
            display = str(self.coffee_drink_size) + ' '
        display += str(self.coffee_drink)
        if self.coffee_place:
            display += ' at ' + str(self.coffee_place)
        return display
    
    class Meta:
        ordering = ['-consumption']
        verbose_name_plural = 'Coffee Logs'