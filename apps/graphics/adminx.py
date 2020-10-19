import xadmin

from .models import Site, Shop, Commodity


class SiteAdmin(object):
    list_display = ['name']
    model_icon = "fa fa-sitemap"


class ShopAdmin(object):
    list_display = ['name', 'site']
    model_icon = "fa fa-shopping-cart"


class CommodityAdmin(object):
    list_display = ['asin', 'rank1', 'rank2', 'score', 'review_number', 'commodity_src', 'shop']
    model_icon = "fa fa-bicycle"


xadmin.site.register(Site, SiteAdmin)
xadmin.site.register(Shop, ShopAdmin)
xadmin.site.register(Commodity, CommodityAdmin)
