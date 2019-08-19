from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=128)

    def __str__(self):
        return "用户" + self.username

    class Meta:
        db_table = 'user'