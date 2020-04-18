from django.db import models
from s_admin.models import AreaModel,RestaurantTypeModel

class ResturantModel(models.Model):
    rest_id = models.AutoField(primary_key=True)
    rest_name = models.CharField(unique=True, max_length=30)
    rest_contact = models.IntegerField(unique=True)
    rest_email = models.EmailField(max_length=100, unique=True)
    rest_area = models.ForeignKey(AreaModel,on_delete=models.CASCADE)
    rest_type =models.ForeignKey(RestaurantTypeModel,on_delete=models.CASCADE)
    rest_password = models.CharField(max_length=30)
    res_otp = models.IntegerField()
    res_status = models.CharField(max_length=30, default=False)