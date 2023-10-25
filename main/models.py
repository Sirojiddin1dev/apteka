from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='user-avatar/', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Banner(models.Model):
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='banner_img/')

    def __str__(self):
        return self.title


class Product(models.Model):
    img = models.ImageField(upload_to='product_img/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Info(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Pharma(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='picture/')

    def __str__(self):
        return self.title

