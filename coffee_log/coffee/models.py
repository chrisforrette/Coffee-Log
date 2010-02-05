from django.db import models
from coffee_log.settings_local import STATUS_OPTIONS

# Coffee Roasters

class CoffeeRoaster(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Roasters'

# Coffee Beans

class CoffeeBean(models.Model):
    roaster = models.ForeignKey(CoffeeRoaster, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    type = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Beans'

# Coffee Drinks

class CoffeeDrink(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return self.name
    
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
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Drink Sizes'

# Coffee Places

class CoffeePlace(models.Model):
    roaster = models.ForeignKey(CoffeeRoaster, blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Coffee Places'

# Coffee Logs

class CoffeeLog(models.Model):
    coffee_drink = models.ForeignKey(CoffeeDrink)
    coffee_bean = models.ForeignKey(CoffeeBean, blank=True, null=True)
    coffee_place = models.ForeignKey(CoffeePlace, blank=True, null=True)
    coffee_drink_size = models.ForeignKey(CoffeeDrinkSize, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    consumption = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default=1)
    
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