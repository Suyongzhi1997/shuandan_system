from django.db import models
from datetime import datetime

from users.models import UserProfile


class Record(models.Model):
    record_status_choices = (
        ("already pay", "已付款"),
        ("no order", "无订单"),
        ("unpaid", "未付款")
    )
    audit_results_choices = (
        ("uncheck", "未审核"),
        ("pass", "通过"),
        ("fail", "未通过")
    )
    brush_status_choices = (
        ("wait submit", "待提交"),
        ("wait check", "待审核"),
        ("already check", "已审核")
    )
    brush_status_two_choices = (
        ("wait send", "待提交"),
        ("already send", "已提交")
    )
    brush_status_three_choices = (
        ("wait send", "待提交"),
        ("already send", "已提交")
    )
    review_type_choices = (
        ("直评", "直评"),
        ("留评", "留评"),
        ("免评", "免评")
    )
    record_settlement_choices = (
        ("settlement", "已结算"),
        ("unsettlement", "未结算")
    )

    asin = models.CharField("ASIN", max_length=100, default='')
    c_price = models.CharField("产品售价", max_length=100, default=0)
    c_price_status = models.BooleanField("售价是否相加", default=False)
    purchase_cost = models.FloatField("采购成本", max_length=100, default=0)
    product_profit = models.FloatField("产品利润", max_length=100, default=0)
    product_upload_time = models.DateTimeField("上架时间", null=True, blank=True)
    brush_number = models.IntegerField("产品刷单总数量", default=0)
    sale_30_number = models.IntegerField("最近30天销量", default=0)
    sale_7_number = models.IntegerField("最近7天销量", default=0)
    review_number = models.CharField("评价数量", max_length=100, default='1')
    feedback = models.CharField("Feedback", max_length=100, default='1')
    direct_review = models.CharField("直评", max_length=100, default='1')
    free_review_number = models.CharField("免评数量", max_length=100, default='1')
    audit_results = models.CharField("审核结果", choices=audit_results_choices, max_length=100, default='uncheck')
    brush_status = models.CharField("刷单状态", choices=brush_status_choices, max_length=100, default='wait submit')
    brush_status_two = models.CharField("刷单状态二", choices=brush_status_two_choices, max_length=100, default='wait send')
    brush_status_three = models.CharField("刷单状态三", choices=brush_status_three_choices, max_length=100,
                                          default='wait send')
    record_src = models.CharField("商品链接", max_length=1000, default='')
    now_score = models.CharField("现在商品星级", max_length=100, default='', null=True, blank=True)
    now_review_number = models.IntegerField("现在商品总评论数", default=0)
    review_type = models.CharField("评论类型", choices=review_type_choices, max_length=100, default='留评')
    remark = models.CharField("备注", max_length=1000, default='')

    site = models.CharField("站点", max_length=100, default='')
    shop = models.CharField("店铺", max_length=100, default='')
    product_chinese_name = models.CharField("产品中文名", max_length=100, default='')
    sku = models.CharField("SKU", max_length=100, default='')
    order_word = models.CharField("刷单词", max_length=100, default='')
    key_word_page_number = models.CharField("关键词的页数", max_length=100, default='')
    main_image = models.ImageField("主图片", upload_to="data/image/%Y/%m", max_length=100, default='')
    key_word_link = models.CharField("关键词链接", max_length=2000, default='')
    brush_company = models.ForeignKey(UserProfile, verbose_name='刷单公司用户', null=True, blank=True,
                                      on_delete=models.CASCADE, related_name='brush_company_users')
    order_number = models.CharField("订单号", max_length=100, default='')
    brush_money = models.FloatField("刷单费用", max_length=100, default=0)
    review_feedback = models.CharField("留评反馈", max_length=1000, default='')
    add_time = models.DateTimeField("提交日期", default=datetime.now)
    user = models.ForeignKey(UserProfile, verbose_name='运营人员', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='company_users')
    record_status = models.CharField("订单状态", choices=record_status_choices, max_length=100, default='no order')
    order_date = models.DateField("下单日期", null=True, blank=True)
    direct_review_title = models.CharField("直评标题", max_length=1000, default='', null=True, blank=True)
    direct_review_content = models.TextField("直评内容", default='', null=True, blank=True)
    review_date = models.DateField("上评日期", null=True, blank=True)
    direct_review_remark = models.CharField("直评备注", max_length=1000, default='', null=True, blank=True)
    record_settlement = models.CharField("结算状态", choices=record_settlement_choices, max_length=100,
                                         default='unsettlement')
    operating_cost = models.FloatField("操作费用", max_length=100, default=0)
    product_cost = models.FloatField("产品费用", max_length=100, default=0)

    class Meta:
        verbose_name = verbose_name_plural = '刷单记录'


class FeedBackRecordUser(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='运营人员', null=True, blank=True, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, verbose_name='刷单记录', null=True, blank=True, on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='提交日期', default=datetime.now)

    class Meta:
        verbose_name = verbose_name_plural = '反馈刷单记录关系'


class UserBrushMoney(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='运营人员', null=True, blank=True, on_delete=models.CASCADE)
    brush_year = models.CharField("年", max_length=100, default=datetime.now().strftime('%Y'))
    brush_month = models.CharField("月", max_length=100, default=datetime.now().strftime('%m'))
    brush_money = models.FloatField("刷单金额", max_length=100, default=0)
    operating_cost = models.FloatField("操作费用", max_length=100, default=0)
    product_cost = models.FloatField("产品费用", max_length=100, default=0)
    add_time = models.DateTimeField("提交日期", default=datetime.now)

    class Meta:
        verbose_name = verbose_name_plural = '每月运营人员刷单金额'


class SumBrushMoney(models.Model):
    brush_year = models.CharField("年", max_length=100, default=datetime.now().strftime('%Y'))
    brush_month = models.CharField("月", max_length=100, default=datetime.now().strftime('%m'))
    brush_money = models.FloatField("刷单金额", max_length=100, default=0)
    operating_cost = models.FloatField("操作费用", max_length=100, default=0)
    product_cost = models.FloatField("产品费用", max_length=100, default=0)
    add_time = models.DateTimeField("提交日期", default=datetime.now)

    class Meta:
        verbose_name = verbose_name_plural = '每月刷单金额'
