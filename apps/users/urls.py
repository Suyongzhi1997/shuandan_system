from django.urls import path, re_path

from .views import EditUserNameView, EditUserPasswordView

app_name = "user"

urlpatterns = [
    path('edit_name/', EditUserNameView.as_view(), name="edit_username"),
    path('edit_password/', EditUserPasswordView.as_view(), name="edit_password"),
]
