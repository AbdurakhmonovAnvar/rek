from django.db import models
from django import db
from users.models import Users


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'region'


class Street(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'street'


class Adver_type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'adver_type'


class Adver(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    type = models.ForeignKey(Adver_type, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    price = models.CharField(max_length=255, default='deactive')
    price_type_choices = [('sum', 'Sum'), ('$', 'Dollar$')]
    price_type = models.CharField(max_length=20, choices=price_type_choices, default='sum')
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'adver'
