from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.views.generic.base import View
from ratelimit.exceptions import Ratelimited

from users.forms import LoginForm


# 登录视图
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.add_message(request, messages.INFO, '用户已登录，请退出后再访问')
            if request.user.username.startswith('yy'):
                return redirect(reverse('deliveries:infos'))
                # return redirect(reverse('record:yy_check_records'))
            elif request.user.username.startswith('sh'):
                return redirect(reverse('record:sh_check_records'))
            elif request.user.username.startswith('sdgs'):
                return redirect(reverse('record:sdgs_brush_records'))
            elif request.user.username.startswith('sd'):
                return redirect(reverse('record:sd_brush_records'))
            else:
                return redirect('/xadmin')
        title = '登录'
        login_form = LoginForm()
        return render(request, 'login.html', {'title': title, 'login_form': login_form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        title = '登录'
        # 获取用户提交的用户名和密码
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # 只有注册激活后才能登录
                    login(request, user)
                    if not user.nick_name:
                        user.nick_name = user.username
                        user.save()
                    if request.user.username.startswith('yy'):
                        # return redirect(reverse('record:yy_check_records'))
                        return redirect(reverse('deliveries:infos'))
                    elif request.user.username.startswith('sh'):
                        return redirect(reverse('record:sh_check_records'))
                    elif request.user.username.startswith('sdgs'):
                        return redirect(reverse('record:sdgs_brush_records'))
                    elif request.user.username.startswith('sd'):
                        return redirect(reverse('record:sd_brush_records'))
                    else:
                        return redirect('/xadmin')
                else:
                    messages.add_message(request, messages.ERROR, '用户未激活', extra_tags='danger')
                    return render(request, 'login.html', {'form': login_form})
            else:
                messages.add_message(request, messages.ERROR, '用户名或密码错误', extra_tags='danger')
                return render(request, 'login.html', {'form': login_form})
        else:
            messages.add_message(request, messages.ERROR, '用户名或密码错误', extra_tags='danger')
            return render(request, 'login.html', {'form': login_form})


# 退出视图
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, '退出成功')
        return HttpResponseRedirect(reverse('login'))


# 编辑用户名
class EditUserNameView(LoginRequiredMixin, View):
    def post(self, request):
        nick_name = request.POST.get('nick_name', '')
        next_url = request.POST.get('next_url', '')
        user = request.user
        user.nick_name = nick_name
        user.save()
        return redirect(next_url)


# 改密码
class EditUserPasswordView(LoginRequiredMixin, View):
    def post(self, request):
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        next_url = request.GET.get('next', '')
        user = request.user
        if password != password2:
            messages.add_message(request, messages.ERROR, "两个密码不一致", extra_tags='danger')
        else:
            user.password = make_password(password2)
            user.save()
        return redirect(next_url)


def pag_not_found(request, exception):
    # 全局404处理函数
    if request.user.username.startswith('yy'):
        return redirect(reverse('record:yy_check_records'))
    elif request.user.username.startswith('sh'):
        return redirect(reverse('record:sh_check_records'))
    elif request.user.username.startswith('sd'):
        return redirect(reverse('record:sd_brush_records'))
    else:
        return redirect(reverse('record:sdgs_brush_records'))


def page_error(request):
    # 全局500处理函数
    if request.user.username.startswith('yy'):
        return redirect(reverse('record:yy_check_records'))
    elif request.user.username.startswith('sh'):
        return redirect(reverse('record:sh_check_records'))
    elif request.user.username.startswith('sd'):
        return redirect(reverse('record:sd_brush_records'))
    else:
        return redirect(reverse('record:sdgs_brush_records'))


def ratelimit_error(request, exception=None):
    if isinstance(exception, Ratelimited):
        data = {
            "url": "http://127.0.0.1:8000/record/sdgs/403/"
        }
        return JsonResponse(data)
        # return render(request, '403.html')
    return HttpResponseForbidden('Forbidden')
