from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2) # so can be up to 9999.99
	description = models.TextField()
	sku = models.CharField(max_length=50)
	image = models.CharField(max_length=128) # i'd do ImageField but I don't want you to see my deets :-/
	thumb = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name