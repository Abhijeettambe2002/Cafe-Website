from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DeliveryInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    landmark = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name
