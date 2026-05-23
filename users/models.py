from django.db import models
from django.contrib.auth.models import AbstractUser

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50) # Basic, Standard, Premium
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video_quality = models.CharField(max_length=50)
    device_limits = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    subscription = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username or self.email
