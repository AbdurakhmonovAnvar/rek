from django.db import models
from users.models import Users


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'a_s'
