# Generated by Django 2.2.9 on 2020-10-19 10:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsCompanyFreight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_company', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='发货公司')),
                ('brush_year', models.CharField(default='2020', max_length=100, verbose_name='年')),
                ('brush_month', models.CharField(default='10', max_length=100, verbose_name='月')),
                ('freight', models.FloatField(default=0, max_length=100, verbose_name='每月运费')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='提交日期')),
            ],
            options={
                'verbose_name': '每月物流公司运费',
                'verbose_name_plural': '每月物流公司运费',
            },
        ),
        migrations.CreateModel(
            name='UserFreight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brush_year', models.CharField(default='2020', max_length=100, verbose_name='年')),
                ('brush_month', models.CharField(default='10', max_length=100, verbose_name='月')),
                ('freight', models.FloatField(default=0, max_length=100, verbose_name='每月运费')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='提交日期')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='运营人员')),
            ],
            options={
                'verbose_name': '每月运营人员运费',
                'verbose_name_plural': '每月运营人员运费',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(blank=True, null=True, verbose_name='发货日期')),
                ('send_company', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='发货公司')),
                ('channel', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='渠道')),
                ('site', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='站点')),
                ('country', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='国家')),
                ('track_number', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='运单追踪号')),
                ('net_weight', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='实重')),
                ('volume_weight', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='材积重')),
                ('actual_charged_weight', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='实际收费重量')),
                ('pieces_number', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='件数')),
                ('includes_price', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='单价包含纺织等的附加费')),
                ('other_price', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='其他附加费用')),
                ('total_price', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='总运费')),
                ('express_time', models.DateTimeField(blank=True, null=True, verbose_name='到货日期')),
                ('express_status', models.CharField(choices=[('already express', '已全部到货'), ('not express', 'no')], default='not express', max_length=100, verbose_name='是否全部到货')),
                ('settlement', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='结算')),
                ('order_remark', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='其他备注')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='运营人员')),
            ],
            options={
                'verbose_name': '物流信息',
                'verbose_name_plural': '物流信息',
            },
        ),
    ]