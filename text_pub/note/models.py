from django.db import models

from user.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    content = models.TextField('内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(User)