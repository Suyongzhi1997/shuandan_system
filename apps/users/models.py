from django.db import models
from django.contrib.auth.models import AbstractUser

"""
使用AbstractUser可以对User进行扩展使用，添加用户自定义的属性。
"""


class UserProfile(AbstractUser):
    avatar = models.ImageField('头像', upload_to='image/avatar', default='image/avatar/default.png')
    nick_name = models.CharField(verbose_name='昵称', max_length=50, default='')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
