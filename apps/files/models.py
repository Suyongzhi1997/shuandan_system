from datetime import datetime

from django.db import models


class File(models.Model):
    # name = models.CharField('文件名', max_length=100)
    excel_file = models.FileField("表格文件", upload_to="data/resource/%Y/%m", max_length=100, default='')
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "资源文件"
        verbose_name_plural = verbose_name
