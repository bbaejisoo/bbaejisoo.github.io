from django.db import models

# Create your models here.
class Play(models.Model):
    original = models.CharField(max_length=30, blank=True, null=True)
    encrypted = models.CharField(max_length=200, blank=True, null=True)
    decrypted = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'play'

class Supermarket(models.Model):
    itemno = models.IntegerField(db_column='Itemno', blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)
    foodname = models.CharField(db_column='FoodName', max_length=30, blank=True, null=True)
    company = models.CharField(db_column='Company', max_length=20, blank=True, null=True)
    price = models.IntegerField(db_column='Price', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supermarket'
