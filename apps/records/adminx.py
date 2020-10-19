import xadmin

from .models import Record, UserBrushMoney, SumBrushMoney


class RecordAdmin(object):
    list_display = ['asin', 'c_price', 'purchase_cost', 'product_profit', 'product_upload_time', 'brush_number',
                    'sale_30_number', 'sale_7_number', 'review_number', 'feedback', 'direct_review',
                    'free_review_number', 'site', 'shop', 'product_chinese_name', 'sku', 'order_number', 'brush_money',
                    'review_feedback', 'add_time']
    search_fields = ['asin', 'shop']
    list_filter = ['asin', 'shop']
    model_icon = 'fa fa-book'


class UserBrushMoneyAdmin(object):
    list_display = ['get_name', 'brush_year', 'brush_month', 'brush_money', 'operating_cost', 'product_cost']
    model_icon = 'fa fa-book'

    def get_name(self, obj):
        return '%s' % obj.user.name


class SumBrushMoneyAdmin(object):
    list_display = ['brush_year', 'brush_month', 'brush_money', 'operating_cost', 'product_cost']
    model_icon = 'fa fa-book'


xadmin.site.register(Record, RecordAdmin)
xadmin.site.register(UserBrushMoney, UserBrushMoneyAdmin)
xadmin.site.register(SumBrushMoney, SumBrushMoneyAdmin)
