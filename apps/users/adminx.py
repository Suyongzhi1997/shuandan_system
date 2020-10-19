import xadmin
from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '刷单统计管理界面'
    # 修改footer
    site_footer = '深圳图贸科技有限公司'


# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)
