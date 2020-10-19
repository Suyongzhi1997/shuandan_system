from datetime import datetime

from django.db import models
from users.models import UserProfile


# Create your models here.
class Product(models.Model):
    status_choices = (('0', '待提交'), ('1', '待完成'), ('2', '已完成'))
    asin = models.CharField(verbose_name="asin", max_length=20)
    content = models.TextField(verbose_name="内容", default="")
    company = models.CharField(verbose_name="公司", max_length=20, null=True, blank=True)
    cost = models.FloatField(verbose_name="费用", null=True, blank=True)
    user = models.ForeignKey(UserProfile, verbose_name='运营人员', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='user_product')
    add_time = models.DateTimeField("提交日期", default=datetime.now)
    sh_remark = models.CharField(verbose_name="审核备注", max_length=5000, null=True, blank=True)
    yy_remark = models.CharField(verbose_name="运营备注", max_length=5000, null=True, blank=True)
    status = models.CharField(max_length=10, choices=status_choices, default='0', verbose_name='状态')
