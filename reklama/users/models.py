from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Users(models.Model):
    # id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='active')
    language = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tg_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = raw_password
        self.save()

    def check_password(self, raw_password):
        a = make_password(self.password)
        return check_password(raw_password, a)

    @property
    def is_active(self):
        return self.status == 'active'

    @property
    def is_authenticated(self):
        return True

    class Meta:
        db_table = 'users'
