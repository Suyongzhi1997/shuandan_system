import xadmin

from .models import Goods


class GoodsAdmin(object):
    list_display = ['send_time', 'send_company', 'channel', 'site', 'user_nick_name', 'country', 'track_number',
                    'total_price',
                    'express_time', 'settlement', 'order_remark']
    search_fields = ['site', 'track_number', 'user__username', 'user__nick_name']
    list_filter = ['send_company', 'site', 'track_number', 'user']
    model_icon = 'fa fa-subway'

    # 显示用户邮箱地址
    def user_nick_name(self, obj):
        return u'%s' % obj.user.nick_name


xadmin.site.register(Goods, GoodsAdmin)
