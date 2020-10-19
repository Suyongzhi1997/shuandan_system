from django.urls import path, re_path
# 要写上app的名字
from .views import InfosView, AddInfoView, EditInfoView, DeleteInfoView, UserFreightView, CompanyFreightView
from django.views.generic import TemplateView

app_name = "deliveries"

urlpatterns = [
    path('infos/', InfosView.as_view(), name="infos"),
    path('add_info/', AddInfoView.as_view(), name="add_info"),
    path('edit_info/', EditInfoView.as_view(), name="edit_info"),
    path('delete_info/', DeleteInfoView.as_view(), name="delete_info"),
    path('user/freight/', UserFreightView.as_view(), name="user_freight"),
    path('company/freight/', CompanyFreightView.as_view(), name="company_freight"),
]
