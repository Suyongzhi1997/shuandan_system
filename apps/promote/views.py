import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.db.models import Q
from django.contrib import messages
from pure_pagination import Paginator

from promote.forms import ProductForm, ShProductForm
from promote.models import Product
from records.models import Record


class ShInfosView(LoginRequiredMixin, View):
    def get(self, request):
        title = "产品信息"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user,
                                                             brush_status='already check').count() if request.user.username.startswith(
            "yy") else Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()

        # 搜索功能
        all_infos = Product.objects.filter(status="1").order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_infos, 9, request=request)
        all_infos = p.page(page)

        return render(request, 'sh_product.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_infos': all_infos
        })


class ShAlreadyInfosView(LoginRequiredMixin, View):
    def get(self, request):
        title = "产品信息"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user,
                                                             brush_status='already check').count() if request.user.username.startswith(
            "yy") else Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()

        # 搜索功能
        all_infos = Product.objects.filter(status="2").order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_infos, 9, request=request)
        all_infos = p.page(page)

        return render(request, 'sh_already_product.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_infos': all_infos
        })


class YyInfosView(LoginRequiredMixin, View):
    def get(self, request):
        title = "产品信息"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user,
                                                             brush_status='already check').count() if request.user.username.startswith(
            "yy") else Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        # 搜索功能
        all_infos = Product.objects.filter(status="0", user=request.user).order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_infos, 9, request=request)
        all_infos = p.page(page)

        return render(request, 'yy_product.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_infos': all_infos
        })


class YyWaitInfosView(LoginRequiredMixin, View):
    def get(self, request):
        title = "产品信息"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user,
                                                             brush_status='already check').count() if request.user.username.startswith(
            "yy") else Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        # 搜索功能
        all_infos = Product.objects.filter(status="1", user=request.user).order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_infos, 9, request=request)
        all_infos = p.page(page)

        return render(request, 'yy_wait_product.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_infos': all_infos
        })


class YyAlreadyInfosView(LoginRequiredMixin, View):
    def get(self, request):
        title = "产品信息"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user,
                                                             brush_status='already check').count() if request.user.username.startswith(
            "yy") else Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        # 搜索功能
        all_infos = Product.objects.filter(status="2", user=request.user).order_by('-add_time')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_infos, 9, request=request)
        all_infos = p.page(page)

        return render(request, 'yy_already_product.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_infos': all_infos
        })


class AddInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = ProductForm(request.POST)
        if form.is_valid():
            asin = request.POST.get('asin', None)
            content = request.POST.get('content', None)
            yy_remark = request.POST.get('yy_remark', None)

            product = Product()
            product.asin = asin
            product.content = content
            product.yy_remark = yy_remark
            product.user = request.user
            product.status = '0'
            product.save()
            return redirect(next_url)
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(form.errors)
            errors_list = re.findall(pattern, errors)
            messages.add_message(request, messages.ERROR, errors_list[0], extra_tags='danger')
            return redirect(next_url)


class EditInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.META['HTTP_REFERER']
        form = ProductForm(request.POST)
        if form.is_valid():
            p_id = request.POST.get('info_id', None)
            asin = request.POST.get('asin', None)
            content = request.POST.get('content', None)
            yy_remark = request.POST.get('yy_remark', None)

            product = Product.objects.get(pk=p_id)
            product.asin = asin
            product.content = content
            product.yy_remark = yy_remark
            product.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class ShEditInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.META['HTTP_REFERER']
        form = ShProductForm(request.POST)
        if form.is_valid():
            p_id = request.POST.get('info_id', None)
            company = request.POST.get('company', None)
            cost = request.POST.get('cost', None)
            sh_remark = request.POST.get('sh_remark', None)

            product = Product.objects.get(pk=p_id)
            product.company = company
            product.cost = cost
            product.sh_remark = sh_remark
            product.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class DeleteInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')

        product_id = request.POST.get("product_id")
        product_object = Product.objects.get(pk=product_id)
        product_object.delete()
        return redirect(next_url)


class SubmitProjectView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_datas = request.POST.get('check_ids')
        project_id_list = [i for i in id_datas.split('_') if i != '']
        for project_id in project_id_list:
            project_object = Product.objects.get(pk=project_id)
            project_object.status = '1'
            project_object.save()
        return redirect(next_url)


class ShSubmitProjectView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_datas = request.POST.get('check_ids')
        project_id_list = [i for i in id_datas.split('_') if i != '']
        for project_id in project_id_list:
            project_object = Product.objects.get(pk=project_id)
            project_object.status = '2'
            project_object.save()
        return redirect(next_url)


class ResetInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')

        product_id = request.POST.get("product_id")
        product_object = Product.objects.get(pk=product_id)
        product_object.status = '0'
        product_object.save()
        return redirect(next_url)


class ShResetProductView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')

        product_id = request.POST.get("product_id")
        product_object = Product.objects.get(pk=product_id)
        product_object.status = '1'
        product_object.save()
        return redirect(next_url)
