from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
