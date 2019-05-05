from django.db import models

# Create your models here.

class DebtManagement1S(models.Model):
    class Meta:
        managed = False
        db_table = 'debt_management1s'
