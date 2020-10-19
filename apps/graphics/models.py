import datetime

from django.db import models


class Site(models.Model):
    name = models.CharField('站点名', max_length=20)
    add_time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = '站点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField('店铺名', max_length=20)
    site = models.ForeignKey(Site, verbose_name='站点', null=True, blank=True, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = '店铺'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Commodity(models.Model):
    asin = models.CharField('asin', max_length=20)
    rank1 = models.CharField('大类排名', max_length=20)
    rank2 = models.CharField('小类排名', max_length=20)
    score = models.CharField('评分', max_length=10)
    review_number = models.CharField('评论数量', max_length=10)
    commodity_src = models.CharField('商品链接', max_length=5000)
    price = models.CharField('商品价格', max_length=20, default="")

    shop = models.ForeignKey(Shop, verbose_name='店铺', null=True, blank=True, on_delete=models.CASCADE)
    add_time = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = '亚马逊商品'
        verbose_name_plural = verbose_name


class Formemory_jp(models.Model):
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class DreamJing_fr(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class DreamJing_uk(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class DreamJing_de(models.Model):
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Houstory_uk(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Houstory_es(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Houstory_it(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Houstory_de(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Housestory_ca(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Housestory_com(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Formemory_ca(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Formemory_com(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class DreamJ_ca(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class DreamJ_com(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Kicpot_ca(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Kicpot_com(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Hapyshop_jp(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Shengo_jp(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class HOM_jp(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Tumao_jp(models.Model):
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class FOR_jp(models.Model):
    """
    法国
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Sakura_jp(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Jiaxingo_jp(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Hezhipu_jp(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Derura_jp(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class HongWan_jp(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Houstory_fr(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Hongfago_de(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Baipin_es(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Ewigkis_es(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Jumping_com(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)


class Rongyio_com(models.Model):
    """
    日本
    """
    asin = models.CharField(verbose_name="asin", max_length=20)
    time = models.DateField(default=datetime.date.today)
    score = models.FloatField(verbose_name="评分")
    comment = models.IntegerField(verbose_name="评论数")
    big = models.IntegerField(verbose_name="大类排名")
    small = models.IntegerField(verbose_name="小类排名")
    price = models.FloatField(verbose_name="价格")
    url = models.CharField(verbose_name="商品链接", max_length=5000)
    name = models.CharField(verbose_name="商品名称", max_length=5000, null=True, blank=True)
