from django.db import models
from datetime import datetime

from users.models import UserProfile


class Goods(models.Model):
    express_status_choice = (
        ("already express", "已全部到货"),
        ("not express", "no")
    )

    send_time = models.DateTimeField("发货日期", null=True, blank=True)
    send_company = models.CharField("发货公司", max_length=100, default="", null=True, blank=True)
    channel = models.CharField("渠道", max_length=100, default="", null=True, blank=True)
    site = models.CharField("站点", max_length=100, default="", null=True, blank=True)
    user = models.ForeignKey(UserProfile, verbose_name='运营人员', null=True, blank=True, on_delete=models.CASCADE)
    country = models.CharField("国家", max_length=100, default="", null=True, blank=True)
    track_number = models.CharField("运单追踪号", max_length=100, default="", null=True, blank=True)
    net_weight = models.CharField("实重", max_length=100, default="", null=True, blank=True)
    volume_weight = models.CharField("材积重", max_length=100, default="", null=True, blank=True)
    actual_charged_weight = models.CharField("实际收费重量", max_length=100, default="", null=True, blank=True)
    pieces_number = models.CharField("件数", max_length=100, default="", null=True, blank=True)
    includes_price = models.CharField("单价包含纺织等的附加费", max_length=100, default="", null=True, blank=True)
    other_price = models.CharField("其他附加费用", max_length=100, default="", null=True, blank=True)
    total_price = models.CharField("总运费", max_length=100, default="", null=True, blank=True)
    express_time = models.DateTimeField("到货日期", null=True, blank=True)
    express_status = models.CharField("是否全部到货", choices=express_status_choice, default="not express", max_length=100)
    settlement = models.CharField("结算", max_length=100, default="", null=True, blank=True)
    order_remark = models.CharField("其他备注", max_length=100, default="", null=True, blank=True)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "物流信息"
        verbose_name_plural = verbose_name


class UserFreight(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='运营人员', null=True, blank=True, on_delete=models.CASCADE)
    brush_year = models.CharField("年", max_length=100, default=datetime.now().strftime('%Y'))
    brush_month = models.CharField("月", max_length=100, default=datetime.now().strftime('%m'))
    freight = models.FloatField("每月运费", max_length=100, default=0)
    add_time = models.DateTimeField("提交日期", default=datetime.now)

    class Meta:
        verbose_name = '每月运营人员运费'
        verbose_name_plural = verbose_name


class LogisticsCompanyFreight(models.Model):
    send_company = models.CharField("发货公司", max_length=100, default="", null=True, blank=True)
    brush_year = models.CharField("年", max_length=100, default=datetime.now().strftime('%Y'))
    brush_month = models.CharField("月", max_length=100, default=datetime.now().strftime('%m'))
    freight = models.FloatField("每月运费", max_length=100, default=0)
    add_time = models.DateTimeField("提交日期", default=datetime.now)

    class Meta:
        verbose_name = '每月物流公司运费'
        verbose_name_plural = verbose_name
