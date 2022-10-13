from django.db import models
from django.contrib.auth.models import User
app_label = 'invoice'

class Invoice(models.Model):
    item_name = models.CharField(max_length=50)
    quantity = models.BigIntegerField(default=1)
    unit_price = models.BigIntegerField(default=1)
    amount = models.BigIntegerField(default=1)
    total_price = models.CharField(max_length=100000,default=0)
    Oracode = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
            return self.item_name
        

    
        

    
