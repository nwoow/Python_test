# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=20)
    delayedprice = models.FloatField(db_column='delayedPrice', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    delayedsize = models.FloatField(db_column='delayedSize', blank=True, null=True)  # Field name made lowercase.
    delayedpricetime = models.FloatField(db_column='delayedPriceTime', blank=True, null=True)  # Field name made lowercase.
    processedtime = models.FloatField(db_column='processedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock'


class Stock1(models.Model):
    delayedprice = models.FloatField(db_column='delayedPrice')  # Field name made lowercase.
    symbol = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Stock1'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
