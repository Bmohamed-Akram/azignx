from django.db import models

# Create your models here.

class service(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField()
    description = models.TextField(max_length=1500)

class projects(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField()
    link = models.URLField()
    project_count = models.CharField(max_length=50)

class contact(models.Model):
    name = models.CharField(max_length=150)
    contact_num = models.CharField(max_length=12)
    email = models.EmailField()
    message = models.TextField(max_length=3000)

class subscribe(models.Model):
    email = models.EmailField()