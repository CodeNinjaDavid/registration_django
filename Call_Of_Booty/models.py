from django.db import models


# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.CharField(max_length=40, blank=False, null=False)
    school = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name