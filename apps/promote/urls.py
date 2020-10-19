from django.urls import path
# 要写上app的名字
# from .views import AddInfoView, EditInfoView, DeleteInfoView
from .views import ShInfosView, YyInfosView, AddInfoView, EditInfoView, DeleteInfoView, ResetInfoView, YyWaitInfosView, \
    YyAlreadyInfosView, SubmitProjectView, ShEditInfoView, ShSubmitProjectView, ShAlreadyInfosView, ShResetProductView

app_name = "promote"

urlpatterns = [
    path('sh_infos/', ShInfosView.as_view(), name="sh_infos"),
    path('sh_already_infos/', ShAlreadyInfosView.as_view(), name="sh_already_infos"),
    path('yy_infos/', YyInfosView.as_view(), name="yy_infos"),
    path('yy_wait_infos/', YyWaitInfosView.as_view(), name="yy_wait_infos"),
    path('yy_already_infos/', YyAlreadyInfosView.as_view(), name="yy_already_infos"),
    path('add_info/', AddInfoView.as_view(), name="add_info"),
    path('edit_info/', EditInfoView.as_view(), name="edit_info"),
    path('sh_edit_info/', ShEditInfoView.as_view(), name="sh_edit_info"),
    path('delete_info/', DeleteInfoView.as_view(), name="delete_info"),
    path('reset_info/', ResetInfoView.as_view(), name="reset_info"),
    path('submit_project/', SubmitProjectView.as_view(), name="submit_project"),
    path('sh_submit_project/', ShSubmitProjectView.as_view(), name="sh_submit_project"),
    path('sh_reset_product/', ShResetProductView.as_view(), name="sh_reset_product"),
]