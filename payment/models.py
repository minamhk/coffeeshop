from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email = models.CharField(max_length=300)
    shipping_address1 = models.CharField(max_length=250,blank=True)
    shipping_address2 = models.CharField(max_length=250,blank=True,null=True)
    shipping_city = models.CharField(max_length=25,blank=True)
    shipping_state = models.CharField(max_length=25,blank=True,null=True)
    shipping_zipcode = models.CharField(max_length=25,blank=True,null=True)
    shipping_country = models.CharField(max_length=25,default='IRAN')

    class Meta:
       verbose_name_plural = 'shipping_address'

    def __str__(self):
        return f'shipping address from {self.full_name}'