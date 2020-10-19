"""shuadan_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from django.urls import path, re_path, include

from shuadan_system.settings import MEDIA_ROOT

from users.views import LoginView, LogoutView
from records.views import IndexView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('xadmin/', xadmin.site.urls),

    path('', LoginView.as_view()),
    path('yy/', IndexView.as_view(), name='index'),
    path('kf/', KaifaIndexView.as_view(), name='kf_index'),

    # record
    path('record/', include('records.urls', namespace='record')),
    path('file/', include('files.urls', namespace='file')),
    path('user/', include('users.urls', namespace='user')),
    path('delivery/', include('delivery.urls', namespace='deliveries')),
    path('promote/', include('promote.urls', namespace='promote')),

    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]

handler404 = 'users.views.pag_not_found'
handler500 = 'users.views.page_error'
handler403 = 'users.views.ratelimit_error'
