
from south.db import db
from django.db import models
from coffee_log.coffee.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'CoffeeLog'
        db.create_table('coffee_coffeelog', (
            ('id', orm['coffee.CoffeeLog:id']),
            ('user', orm['coffee.CoffeeLog:user']),
            ('coffee_drink', orm['coffee.CoffeeLog:coffee_drink']),
            ('coffee_bean', orm['coffee.CoffeeLog:coffee_bean']),
            ('coffee_place', orm['coffee.CoffeeLog:coffee_place']),
            ('coffee_drink_size', orm['coffee.CoffeeLog:coffee_drink_size']),
            ('is_homemade', orm['coffee.CoffeeLog:is_homemade']),
            ('notes', orm['coffee.CoffeeLog:notes']),
            ('consumption', orm['coffee.CoffeeLog:consumption']),
            ('created', orm['coffee.CoffeeLog:created']),
            ('modified', orm['coffee.CoffeeLog:modified']),
            ('status', orm['coffee.CoffeeLog:status']),
        ))
        db.send_create_signal('coffee', ['CoffeeLog'])
        
        # Adding model 'CoffeeDrinkSize'
        db.create_table('coffee_coffeedrinksize', (
            ('id', orm['coffee.CoffeeDrinkSize:id']),
            ('name', orm['coffee.CoffeeDrinkSize:name']),
            ('slug', orm['coffee.CoffeeDrinkSize:slug']),
            ('created', orm['coffee.CoffeeDrinkSize:created']),
            ('modified', orm['coffee.CoffeeDrinkSize:modified']),
            ('status', orm['coffee.CoffeeDrinkSize:status']),
        ))
        db.send_create_signal('coffee', ['CoffeeDrinkSize'])
        
        # Adding model 'CoffeeRoaster'
        db.create_table('coffee_coffeeroaster', (
            ('id', orm['coffee.CoffeeRoaster:id']),
            ('name', orm['coffee.CoffeeRoaster:name']),
            ('slug', orm['coffee.CoffeeRoaster:slug']),
            ('url', orm['coffee.CoffeeRoaster:url']),
            ('created', orm['coffee.CoffeeRoaster:created']),
            ('modified', orm['coffee.CoffeeRoaster:modified']),
            ('status', orm['coffee.CoffeeRoaster:status']),
        ))
        db.send_create_signal('coffee', ['CoffeeRoaster'])
        
        # Adding model 'CoffeePlaceCategory'
        db.create_table('coffee_coffeeplacecategory', (
            ('id', orm['coffee.CoffeePlaceCategory:id']),
            ('name', orm['coffee.CoffeePlaceCategory:name']),
            ('slug', orm['coffee.CoffeePlaceCategory:slug']),
            ('created', orm['coffee.CoffeePlaceCategory:created']),
            ('modified', orm['coffee.CoffeePlaceCategory:modified']),
            ('status', orm['coffee.CoffeePlaceCategory:status']),
        ))
        db.send_create_signal('coffee', ['CoffeePlaceCategory'])
        
        # Adding model 'CoffeePlace'
        db.create_table('coffee_coffeeplace', (
            ('id', orm['coffee.CoffeePlace:id']),
            ('roaster', orm['coffee.CoffeePlace:roaster']),
            ('name', orm['coffee.CoffeePlace:name']),
            ('slug', orm['coffee.CoffeePlace:slug']),
            ('address', orm['coffee.CoffeePlace:address']),
            ('city', orm['coffee.CoffeePlace:city']),
            ('state', orm['coffee.CoffeePlace:state']),
            ('zip', orm['coffee.CoffeePlace:zip']),
            ('created', orm['coffee.CoffeePlace:created']),
            ('modified', orm['coffee.CoffeePlace:modified']),
            ('status', orm['coffee.CoffeePlace:status']),
        ))
        db.send_create_signal('coffee', ['CoffeePlace'])
        
        # Adding model 'CoffeePlaceGeoPoint'
        db.create_table('coffee_coffeeplacegeopoint', (
            ('id', orm['coffee.CoffeePlaceGeoPoint:id']),
            ('coffee_place', orm['coffee.CoffeePlaceGeoPoint:coffee_place']),
            ('geo_address', orm['coffee.CoffeePlaceGeoPoint:geo_address']),
            ('geo_point', orm['coffee.CoffeePlaceGeoPoint:geo_point']),
            ('created', orm['coffee.CoffeePlaceGeoPoint:created']),
            ('modified', orm['coffee.CoffeePlaceGeoPoint:modified']),
        ))
        db.send_create_signal('coffee', ['CoffeePlaceGeoPoint'])
        
        # Adding model 'CoffeeBean'
        db.create_table('coffee_coffeebean', (
            ('id', orm['coffee.CoffeeBean:id']),
            ('roaster', orm['coffee.CoffeeBean:roaster']),
            ('name', orm['coffee.CoffeeBean:name']),
            ('slug', orm['coffee.CoffeeBean:slug']),
            ('type', orm['coffee.CoffeeBean:type']),
            ('created', orm['coffee.CoffeeBean:created']),
            ('modified', orm['coffee.CoffeeBean:modified']),
            ('status', orm['coffee.CoffeeBean:status']),
        ))
        db.send_create_signal('coffee', ['CoffeeBean'])
        
        # Adding model 'CoffeeDrink'
        db.create_table('coffee_coffeedrink', (
            ('id', orm['coffee.CoffeeDrink:id']),
            ('name', orm['coffee.CoffeeDrink:name']),
            ('slug', orm['coffee.CoffeeDrink:slug']),
            ('created', orm['coffee.CoffeeDrink:created']),
            ('modified', orm['coffee.CoffeeDrink:modified']),
            ('status', orm['coffee.CoffeeDrink:status']),
        ))
        db.send_create_signal('coffee', ['CoffeeDrink'])
        
        # Adding ManyToManyField 'CoffeePlace.coffee_place_categories'
        db.create_table('coffee_coffeeplace_coffee_place_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coffeeplace', models.ForeignKey(orm.CoffeePlace, null=False)),
            ('coffeeplacecategory', models.ForeignKey(orm.CoffeePlaceCategory, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'CoffeeLog'
        db.delete_table('coffee_coffeelog')
        
        # Deleting model 'CoffeeDrinkSize'
        db.delete_table('coffee_coffeedrinksize')
        
        # Deleting model 'CoffeeRoaster'
        db.delete_table('coffee_coffeeroaster')
        
        # Deleting model 'CoffeePlaceCategory'
        db.delete_table('coffee_coffeeplacecategory')
        
        # Deleting model 'CoffeePlace'
        db.delete_table('coffee_coffeeplace')
        
        # Deleting model 'CoffeePlaceGeoPoint'
        db.delete_table('coffee_coffeeplacegeopoint')
        
        # Deleting model 'CoffeeBean'
        db.delete_table('coffee_coffeebean')
        
        # Deleting model 'CoffeeDrink'
        db.delete_table('coffee_coffeedrink')
        
        # Dropping ManyToManyField 'CoffeePlace.coffee_place_categories'
        db.delete_table('coffee_coffeeplace_coffee_place_categories')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'coffee.coffeebean': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'roaster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.CoffeeRoaster']", 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'coffee.coffeedrink': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'})
        },
        'coffee.coffeedrinksize': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'})
        },
        'coffee.coffeelog': {
            'coffee_bean': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.CoffeeBean']", 'null': 'True', 'blank': 'True'}),
            'coffee_drink': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.CoffeeDrink']"}),
            'coffee_drink_size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.CoffeeDrinkSize']", 'null': 'True', 'blank': 'True'}),
            'coffee_place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.CoffeePlace']", 'null': 'True', 'blank': 'True'}),
            'consumption': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_homemade': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2', 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'coffee.coffeeplace': {
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'coffee_place_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coffee.CoffeePlaceCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'roaster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.CoffeeRoaster']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'coffee.coffeeplacecategory': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'})
        },
        'coffee.coffeeplacegeopoint': {
            'coffee_place': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['coffee.CoffeePlace']", 'unique': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'geo_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geo_point': ('geo_models.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'coffee.coffeeroaster': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['coffee']
