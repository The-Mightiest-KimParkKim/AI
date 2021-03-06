from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.fields import JSONField



# 현재 식재료 
class Grocery(models.Model):
    id = models.AutoField(primary_key=True) #PK(현재식재료PK)
    email = models.CharField(max_length=50, null=True) # FK(사용자id값)
    all_grocery_id = models.IntegerField(blank=True, null=True) # FK(식료품id값)
    name = models.CharField(max_length=20, null=True)
    count = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    gubun = models.IntegerField(blank=True, null=True)
    coordinate = models.JSONField(null=True)
    # coordinate = models.CharField(max_length=500, null=True)
    # coordinate = JSONField

    class Meta:
        db_table = 'GROCERY'

    def __str__(self):
        return '{0}'.format(self.reg_date)

# class Coordinate(models.Model):
#     x = models.FloatField(blank=True, null=True)
#     y = models.FloatField(blank=True, null=True)

#     class Meta:
#         db_table = 'COORDINATE'

#     def __str__(self):
#         return self.x
