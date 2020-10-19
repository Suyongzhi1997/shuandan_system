import re
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from pure_pagination import Paginator
from django.contrib import messages

from records.forms import OperationRecordForm, UploadImageForm, CheckRecordForm, BrushEditForm, SdgsBrushEditForm, \
    DirectReviewForm
from records.models import Record, FeedBackRecordUser, UserBrushMoney, SumBrushMoney

# 运营首页
from users.models import UserProfile


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        title = '刷单提交'
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user, brush_status='already check').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        all_records = Record.objects.filter(user=request.user, brush_status='already check', audit_results='pass',
                                            brush_status_two='wait send').order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # icontains是包含的意思（不区分大小写）
            # Q可以实现多个字段，之间是or的关系
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_records, 5, request=request)
        records = p.page(page)

        return render(request, 'index.html', {
            'already_check_records_number': already_check_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 运营审核提交页面
class YyCheckRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('yy'):
            return redirect('login')
        title = "审核提交"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user, brush_status='already check').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        # 筛选出第一次等待提交的记录
        all_records = Record.objects.filter(user=request.user, brush_status='wait submit').order_by('-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # icontains是包含的意思（不区分大小写）
            # Q可以实现多个字段，之间是or的关系
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        return render(request, 'yy_check_records.html', {
            'already_check_records_number': already_check_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 运营等待审核页面
class YyWaitCheckRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('yy'):
            return redirect('login')
        title = "等待审核"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user, brush_status='already check').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        # 筛选出第一次等待审核的记录
        all_records = Record.objects.filter(user=request.user, brush_status='wait check').order_by('-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # icontains是包含的意思（不区分大小写）
            # Q可以实现多个字段，之间是or的关系
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        return render(request, 'yy_wait_check_records.html', {
            'already_check_records_number': already_check_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 运营已审核页面
class YyAlreadyCheckRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('yy'):
            return redirect('login')
        title = "已审核"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user, brush_status='already check').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        # 筛选出已经审核过的记录
        all_records = Record.objects.filter(user=request.user, brush_status='already check').order_by('-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # icontains是包含的意思（不区分大小写）
            # Q可以实现多个字段，之间是or的关系
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        return render(request, 'yy_already_check_records.html', {
            'already_check_records_number': already_check_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 运营重新提交
class YyResetCommitView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        record_id = request.POST.get('record_id', '')
        record_object = Record.objects.get(pk=record_id)

        new_record_object = Record()
        new_record_object.asin = record_object.asin
        new_record_object.c_price = record_object.c_price
        new_record_object.purchase_cost = record_object.purchase_cost
        new_record_object.product_profit = record_object.product_profit
        new_record_object.product_upload_time = record_object.product_upload_time
        new_record_object.brush_number = record_object.brush_number
        new_record_object.sale_30_number = record_object.sale_30_number
        new_record_object.sale_7_number = record_object.sale_7_number
        new_record_object.review_number = record_object.review_number
        new_record_object.feedback = record_object.feedback
        new_record_object.direct_review = record_object.direct_review
        new_record_object.free_review_number = record_object.free_review_number
        new_record_object.site = record_object.site
        new_record_object.shop = record_object.shop
        new_record_object.product_chinese_name = record_object.product_chinese_name
        new_record_object.sku = record_object.sku
        new_record_object.order_word = record_object.order_word
        new_record_object.key_word_page_number = record_object.key_word_page_number
        new_record_object.main_image = record_object.main_image
        new_record_object.key_word_link = record_object.key_word_link
        new_record_object.user = record_object.user

        new_record_object.save()

        return redirect(next_url)


# 运营刷单提交
class YySubmitBrushView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('check_ids')
        record_id_list = [i for i in id_data.split('_') if i != '']

        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_object.brush_status_two = 'already send'
            record_object.save()

        return redirect(next_url)


# 运营提交审核
class SubmitCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('check_ids')
        record_id_list = [i for i in id_data.split('_') if i != '']

        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_object.brush_status = 'wait check'
            record_object.save()

        return redirect(next_url)


# 运营反馈页面
class YyFeedBackView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('yy'):
            return redirect('login')
        title = "反馈"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user, brush_status='already check').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()

        all_records = Record.objects.filter(user=request.user).filter(~Q(order_number='')).order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # icontains是包含的意思（不区分大小写）
            # Q可以实现多个字段，之间是or的关系
            all_records = all_records.filter(asin__icontains=search_keywords)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 4, request=request)
        records = p.page(page)

        return render(request, 'yy_feedback.html', {
            'already_check_records_number': already_check_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_records': records
        })


class YyFeedbackRecordEditView(LoginRequiredMixin, View):
    def post(self, request):
        record_id = request.POST.get('record_id', '')
        record_status = request.POST.get('record_status', '')
        next_url = request.GET.get('next', '')
        record_object = Record.objects.get(pk=record_id)
        record_object.record_status = record_status
        record_object.save()
        return redirect(next_url)


# 运营刷单费用页面
class YyBrushMoneyView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('yy'):
            return redirect('login')
        title = "刷单费用页面"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user, brush_status='already check').count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()
        brush_moneys = UserBrushMoney.objects.filter(user=user).order_by('-add_time')

        return render(request, 'brush_money.html', {
            'already_check_records_number': already_check_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'brush_moneys': brush_moneys
        })


# 运营直评修改
class YyDirectReviewEditView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = DirectReviewForm(request.POST)
        if form.is_valid():
            record_id = request.POST.get('record_id', '')
            direct_review_title = request.POST.get('direct_review_title', '')
            direct_review_content = request.POST.get('direct_review_content', '')
            direct_review_remark = request.POST.get('direct_review_remark', '')

            record_object = Record.objects.get(pk=record_id)
            record_object.direct_review_title = direct_review_title
            record_object.direct_review_content = direct_review_content
            record_object.direct_review_remark = direct_review_remark

            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


# 审核人审核页面
class ShCheckRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sh'):
            return redirect('login')
        title = "审核"
        user = request.user
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        all_records = Record.objects.filter(brush_status='wait check').order_by('-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # icontains是包含的意思（不区分大小写）
            # Q可以实现多个字段，之间是or的关系
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        return render(request, 'sh_check_records.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 审核人审核
class ShSubmitCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('check_ids')
        check_result_data = request.POST.get('check_datas')
        record_id_list = [i for i in id_data.split('_') if i != '']
        check_result_list = [i for i in check_result_data.split('_') if i != '']
        for num, record_id in enumerate(record_id_list):
            record_object = Record.objects.get(pk=record_id)
            record_object.audit_results = check_result_list[num]
            record_object.brush_status = 'already check'
            record_object.save()

        return redirect(next_url)


# modal提交审核
class ShCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        record_id = request.POST.get('record_id', '')
        audit_results = request.POST.get('audit_results', '')
        remark = request.POST.get('remark', '')
        record_object = Record.objects.get(pk=record_id)
        record_object.audit_results = audit_results
        record_object.remark = remark
        record_object.brush_status = 'already check'
        record_object.save()
        return redirect(next_url)


# 审核人已审核页面
class ShAlreadyCheckRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sh'):
            return redirect('login')
        title = "已审核"
        user = request.user
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        all_records = Record.objects.filter(brush_status='already check', audit_results="pass").order_by('-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        return render(request, 'sh_already_check_records.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 审核人撤销审核
class ShResetCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        record_id = request.POST.get('record_id', '')
        record_object = Record.objects.get(pk=record_id)
        record_object.brush_status = 'wait check'
        record_object.audit_results = 'uncheck'
        record_object.save()
        return redirect(next_url)


# 审核人撤销审核批量
class ShResetChecksView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('check_ids')
        record_id_list = [i for i in id_data.split('_') if i != '']

        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_object.brush_status = 'wait check'
            record_object.audit_results = 'uncheck'
            record_object.save()

        return redirect(next_url)


class ShDeleteRecordsView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('delete_check_ids')
        record_id_list = [i for i in id_data.split('_') if i != '']

        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_object.delete()

        return redirect(next_url)


# 审核人刷单费用页面
class ShBrushMoneyView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sh'):
            return redirect('login')
        title = "刷单费用"
        user = request.user
        brush_moneys = UserBrushMoney.objects.all().order_by('-add_time')
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_type == 'datetime':
            try:
                date_list = [i for i in search_keywords.split('-')]
                brush_moneys = brush_moneys.filter(brush_year=date_list[0], brush_month=date_list[1]).order_by(
                    '-brush_money')
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请填写正确的日期时间", extra_tags='danger')
                return redirect(reverse("record:brush_money"))
        elif search_type == 'people':
            brush_moneys = brush_moneys.filter(
                Q(user__username__icontains=search_keywords) | Q(user__nick_name__icontains=search_keywords))

        return render(request, 'sh_brush_money.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'brush_moneys': brush_moneys
        })


# 审核人刷单撤回
class ShResetBrush(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        record_id = request.POST.get('record_id', '')
        record_object = Record.objects.get(pk=record_id)
        record_object.brush_status_two = 'wait send'
        record_object.save()

        return redirect(next_url)


# 审核人审核撤回
class ShReturnCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        record_id = request.POST.get('record_id', '')
        record_object = Record.objects.get(pk=record_id)
        record_object.brush_status = 'wait submit'
        record_object.save()

        return redirect(next_url)


# 审核人刷单总费用页面
class ShSumBrushMoneyView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sh'):
            return redirect('login')
        title = "刷单总费用"
        user = request.user
        brush_moneys = SumBrushMoney.objects.all().order_by('-add_time')
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        return render(request, 'sum_brush_money.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'brush_moneys': brush_moneys
        })


# 审核搜索记录页面
class ShSearchRecords(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sh'):
            return redirect('login')
        title = "刷单记录"
        user = request.user
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        all_records = Record.objects.filter(~Q(order_number='')).order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_type == 'datetime':
            try:
                date_list = [int(i) for i in search_keywords.split('-')]
                all_records = all_records.filter(add_time__year=date_list[0], add_time__month=date_list[1])
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请填写正确的日期时间", extra_tags='danger')
                return redirect(reverse("record:feedback"))
        elif search_type == 'people':
            all_records = all_records.filter(
                Q(user__username__icontains=search_keywords) | Q(user__nick_name__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个

        if not search_type:
            p = Paginator(all_records, 4, request=request)
        else:
            p = Paginator(all_records, 10000, request=request)
        records = p.page(page)

        return render(request, 'sh_search_records.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 刷单人刷单页面
class SdBrushRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        title = "等待提交"
        user = request.user
        companies = UserProfile.objects.filter(username__istartswith='sdgs')
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        all_records = Record.objects.filter(brush_status_two='already send', brush_status_three='wait send').order_by(
            '-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        html = 'sh_brush_records.html' if request.user.username.startswith('sh') else 'sd_brush_records.html'
        return render(request, html, {
            'companies': companies,
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 刷单提交
class SdSubmitBrushView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('check_ids')
        record_id_list = [i for i in id_data.split('_') if i != '']

        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_object.brush_status_three = 'already send'
            record_object.save()

        return redirect(next_url)


# 刷单已提交页面
class SdAlreadyCheckRecords(LoginRequiredMixin, View):
    def get(self, request):
        title = "已提交"
        user = request.user
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        all_records = Record.objects.filter(brush_status_three='already send').order_by('-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_records = all_records.filter(asin__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)

        html = 'sh_already_brush_records.html' if request.user.username.startswith(
            'sh') else 'sd_already_check_records.html'
        return render(request, html, {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 刷单撤回
class SdResetCheck(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        record_id = request.POST.get('record_id')
        record_object = Record.objects.get(pk=record_id)
        record_object.brush_status_three = 'wait send'
        record_object.save()

        return redirect(next_url)


# 刷单model撤回
class SdResetChecks(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        id_data = request.POST.get('check_ids')
        record_id_list = [i for i in id_data.split('_') if i != '']

        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_object.brush_status_three = 'wait send'
            record_object.save()

        return redirect(next_url)


# 刷单搜索记录页面
class SdSearchRecords(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sd'):
            return redirect('login')
        title = "刷单记录"
        user = request.user
        already_check_records_number = Record.objects.filter(brush_status_three='already send').count()
        all_records = Record.objects.filter(~Q(order_number='')).order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_type == 'datetime':
            try:
                date_list = [int(i) for i in search_keywords.split('-')]
                all_records = all_records.filter(add_time__year=date_list[0], add_time__month=date_list[1])
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请填写正确的日期时间", extra_tags='danger')
                return redirect(reverse("record:feedback"))
        elif search_type == 'people':
            all_records = all_records.filter(
                Q(user__username__icontains=search_keywords) | Q(user__nick_name__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个

        if not search_type:
            p = Paginator(all_records, 4, request=request)
        else:
            p = Paginator(all_records, 10000, request=request)
        records = p.page(page)

        return render(request, 'sd_search_records.html', {
            'already_check_records_number': already_check_records_number,
            'title': title,
            'user': user,
            'all_records': records
        })


# 刷单公司订单页面
class SdgsBrushRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.username.startswith('sdgs') and not request.user.username.startswith('sh'):
            return redirect('login')
        title = "订单"
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        user = request.user
        if request.user.username.startswith("sh"):
            all_records = Record.objects.filter(brush_status_three='already send').order_by('-add_time')
        else:
            all_records = Record.objects.filter(brush_status_three='already send', brush_company=user).order_by(
                '-add_time')
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_records = all_records.filter(asin__icontains=search_keywords)

        filter_type = request.GET.get('filter_type', '')
        if filter_type:
            all_records = all_records.filter(record_settlement=filter_type)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_records, 9, request=request)
        records = p.page(page)
        html = "sh_sdgs_brush_records.html" if request.user.username.startswith("sh") else "sdgs_brush_records.html"
        return render(request, html, {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'all_records': records,
            'filter_type': filter_type
        })


# 刷单公司编辑页面
class SdgsBrushEdit(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = SdgsBrushEditForm(request.POST)
        if form.is_valid():
            record_id = request.POST.get('record_id', '')
            record_object = Record.objects.get(pk=record_id)

            brush_company = request.POST.get('brush_company', '')
            if brush_company:
                brush_company_object = UserProfile.objects.get(pk=brush_company)
                record_object.brush_company = brush_company_object

            order_number = request.POST.get('order_number', '')
            record_object.order_number = order_number

            # 刷单费用
            brush_money = float(request.POST.get('brush_money', 0))
            # 刷单费用的差
            brush_money_difference = brush_money - record_object.brush_money

            # 产品售价
            c_price = 0
            if not record_object.c_price_status:
                price_regex = re.compile("\d+\.?\d+")
                c_price_list = price_regex.findall(record_object.c_price)
                if c_price_list:
                    c_price = float(c_price_list[0])
                    record_object.c_price_status = True

            year = datetime.datetime.now().strftime('%Y')
            month = datetime.datetime.now().strftime('%m')
            user_brush_money = UserBrushMoney.objects.filter(brush_year=year, brush_month=month,
                                                             user=record_object.user).first()
            sum_brush_money = SumBrushMoney.objects.filter(brush_year=year, brush_month=month).first()
            if not sum_brush_money:
                sum_brush_money_object = SumBrushMoney()
            else:
                sum_brush_money_object = sum_brush_money
            sum_brush_money_object.brush_money += round(brush_money_difference, 2)
            sum_brush_money_object.product_cost += round(c_price, 2)
            sum_brush_money_object.save()

            # 如果没有这条记录，先去创建这条记录
            if not user_brush_money:
                user_brush_money_object = UserBrushMoney()
                user_brush_money_object.user = record_object.user
            else:
                user_brush_money_object = user_brush_money
            user_brush_money_object.brush_money += round(brush_money_difference, 2)
            user_brush_money_object.product_cost += round(c_price, 2)
            user_brush_money_object.save()

            record_object.brush_money = brush_money

            review_feedback = request.POST.get('review_feedback', '')
            record_object.review_feedback = review_feedback

            record_status = request.POST.get('record_status', '')
            record_object.record_status = record_status

            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


# 审核刷单公司编辑页面
class ShSdgsBrushEdit(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = SdgsBrushEditForm(request.POST)
        if form.is_valid():
            record_id = request.POST.get('record_id', '')
            record_object = Record.objects.get(pk=record_id)

            order_number = request.POST.get('order_number', '')
            record_object.order_number = order_number

            brush_money = float(request.POST.get('brush_money', 0))
            year = datetime.datetime.now().strftime('%Y')
            month = datetime.datetime.now().strftime('%m')
            user_brush_money = UserBrushMoney.objects.filter(brush_year=year, brush_month=month,
                                                             user=record_object.user).first()
            sum_brush_money = SumBrushMoney.objects.filter(brush_year=year, brush_month=month).first()
            brush_money_difference = brush_money - record_object.brush_money
            # 产品售价
            c_price = 0
            if not record_object.c_price_status:
                price_regex = re.compile("\d+\.?\d+")
                c_price_list = price_regex.findall(record_object.c_price)
                if c_price_list:
                    c_price = float(c_price_list[0])
                    record_object.c_price_status = True

            # 公司总刷单费用
            if not sum_brush_money:
                sum_brush_money_object = SumBrushMoney()
            else:
                sum_brush_money_object = sum_brush_money

            sum_brush_money_object.brush_money += brush_money_difference
            sum_brush_money_object.product_cost += c_price
            sum_brush_money_object.save()

            # 如果没有这条记录，先去创建这条记录
            if not user_brush_money:
                user_brush_money_object = UserBrushMoney()
            else:
                user_brush_money_object = user_brush_money

            user_brush_money_object.brush_money += brush_money_difference
            user_brush_money_object.product_cost += c_price
            user_brush_money_object.save()

            record_object.brush_money = brush_money

            review_feedback = request.POST.get('review_feedback', '')
            record_object.review_feedback = review_feedback

            record_status = request.POST.get('record_status', '')
            record_object.record_status = record_status

            record_settlement = request.POST.get('record_settlement', '')
            record_object.record_settlement = record_settlement

            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class Sdgs403View(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, '403.html')


# 反馈页面
class FeedBackView(LoginRequiredMixin, View):
    def get(self, request):
        title = "刷单记录"
        user = request.user

        all_records = Record.objects.all().order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_type == 'datetime':
            try:
                date_list = [int(i) for i in search_keywords.split('-')]
                all_records = all_records.filter(add_time__year=date_list[0], add_time__month=date_list[1])
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请填写正确的日期时间", extra_tags='danger')
                return redirect(reverse("record:feedback"))
        elif search_type == 'people':
            all_records = all_records.filter(user__username__icontains=search_keywords)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个

        if not search_type:
            p = Paginator(all_records, 3, request=request)
        else:
            p = Paginator(all_records, 10000, request=request)
        records = p.page(page)

        return render(request, 'feedback.html', {
            'title': title,
            'user': user,
            'all_records': records
        })


# 反馈收藏
class FeedBackRecordsView(LoginRequiredMixin, View):
    def get(self, request):
        title = "反馈收藏"
        user = request.user

        all_records = FeedBackRecordUser.objects.filter(user=request.user).order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_type == 'datetime':
            try:
                date_list = [int(i) for i in search_keywords.split('-')]
                all_records = all_records.filter(record__add_time__year=date_list[0],
                                                 record__add_time__month=date_list[1])
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请填写正确的日期时间", extra_tags='danger')
                return redirect(reverse("record:feedback_records"))
        elif search_type == 'people':
            all_records = all_records.filter(user__username__icontains=search_keywords)
        else:
            all_records = all_records.filter(record__asin__icontains=search_keywords)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        if not search_type:
            p = Paginator(all_records, 3, request=request)
        else:
            p = Paginator(all_records, 10000, request=request)
        records = p.page(page)

        html_name = 'yy_fb_favorite.html' if 'yy' in request.user.username else 'fb_favorite.html'

        return render(request, html_name, {
            'title': title,
            'user': user,
            'all_records': records
        })


class FeedBackUnFavoriteRecordView(LoginRequiredMixin, View):
    def get(self, request):
        next_url = request.GET.get('next')
        id_data = request.GET.get('id_data')
        record_id_list = [i for i in id_data.split('_') if i != '']

        flag = False
        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            record_user = FeedBackRecordUser.objects.filter(record=record_object, user=request.user).first()

            if record_user:
                record_user.delete()
                flag = True

        if flag:
            messages.add_message(request, messages.SUCCESS, "取消收藏成功", extra_tags='success')
        data = {
            "next_url": next_url
        }
        return JsonResponse(data)


# 开发首页
class KaifaIndexView(LoginRequiredMixin, View):
    def get(self, request):
        title = "首页"
        user = request.user

        all_records = Record.objects.all().order_by('-add_time')

        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_type == 'datetime':
            try:
                date_list = [int(i) for i in search_keywords.split('-')]
                all_records = all_records.filter(add_time__year=date_list[0], add_time__month=date_list[1])
            except Exception as e:
                messages.add_message(request, messages.ERROR, "请填写正确的日期时间", extra_tags='danger')
                return redirect(reverse("record:kf_index"))
        elif search_type == 'people':
            all_records = all_records.filter(user__username__icontains=search_keywords)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        if not search_type:
            p = Paginator(all_records, 3, request=request)
        else:
            p = Paginator(all_records, 10000, request=request)

        records = p.page(page)

        return render(request, 'kaifa_index.html', {
            'title': title,
            'user': user,
            'all_records': records
        })


class AddCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.META['HTTP_REFERER']
        form = CheckRecordForm(request.POST)
        if form.is_valid():
            asin = request.POST.get('ASIN', '')
            c_price = request.POST.get('c_price', '')
            purchase_cost = request.POST.get('purchase_cost', '')
            product_profit = request.POST.get('product_profit', '')
            product_upload_time = request.POST.get('product_upload_time', '')
            # brush_number = request.POST.get('brush_number', '')
            sale_30_number = request.POST.get('sale_30_number', '')
            sale_7_number = request.POST.get('sale_7_number', '')
            record_src = request.POST.get('record_src', '')
            review_type = request.POST.get('review_type', '')
            now_score = request.POST.get('now_score', '')
            now_review_number = request.POST.get('now_review_number', 0)

            record_object = Record()
            record_object.asin = asin
            record_object.c_price = c_price
            record_object.purchase_cost = purchase_cost
            record_object.product_profit = product_profit
            record_object.product_upload_time = product_upload_time
            record_object.sale_30_number = sale_30_number
            record_object.sale_7_number = sale_7_number
            record_object.record_src = record_src
            record_object.review_type = review_type
            if review_type == "留评":
                record_object.review_number = '1'
                record_object.direct_review = '0'
                record_object.free_review_number = '0'
                record_object.feedback = '0'
            elif review_type == "直评":
                record_object.direct_review = '1'
                record_object.review_number = '0'
                record_object.free_review_number = '0'
                record_object.feedback = '0'
            elif review_type == "免评":
                record_object.free_review_number = '1'
                record_object.review_number = '0'
                record_object.direct_review = '0'
                record_object.feedback = '0'
            elif review_type == "feedback":
                record_object.free_review_number = '0'
                record_object.review_number = '0'
                record_object.direct_review = '0'
                record_object.feedback = '1'

            record_object.now_score = now_score
            record_object.now_review_number = now_review_number
            record_object.user = request.user
            record_object.save()
            return redirect(next_url)
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(form.errors)
            errors_list = re.findall(pattern, errors)
            messages.add_message(request, messages.ERROR, errors_list[0], extra_tags='danger')
            return redirect(next_url)


# 运营修改待审核记录
class EditCheckView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = CheckRecordForm(request.POST)
        if form.is_valid():
            record_id = request.POST.get('record_id', '')
            asin = request.POST.get('ASIN', '')
            c_price = request.POST.get('c_price', '')
            purchase_cost = request.POST.get('purchase_cost', '')
            product_profit = request.POST.get('product_profit', '')
            product_upload_time = request.POST.get('product_upload_time', '')
            # brush_number = request.POST.get('brush_number', '')
            sale_30_number = request.POST.get('sale_30_number', '')
            sale_7_number = request.POST.get('sale_7_number', '')
            # feedback = request.POST.get('Feedback', '')
            record_src = request.POST.get('record_src', '')
            review_type = request.POST.get('review_type', '')
            now_score = request.POST.get('now_score', '')
            now_review_number = request.POST.get('now_review_number', 0)

            record_object = Record.objects.get(pk=record_id)
            record_object.asin = asin
            record_object.c_price = c_price
            record_object.purchase_cost = purchase_cost
            record_object.product_profit = product_profit
            record_object.product_upload_time = product_upload_time
            # record_object.brush_number = brush_number
            record_object.sale_30_number = sale_30_number
            record_object.sale_7_number = sale_7_number
            record_object.record_src = record_src
            record_object.review_type = review_type
            if review_type == "留评":
                record_object.review_number = '1'
                record_object.direct_review = '0'
                record_object.free_review_number = '0'
                record_object.feedback = '0'
            elif review_type == "直评":
                record_object.direct_review = '1'
                record_object.review_number = '0'
                record_object.free_review_number = '0'
                record_object.feedback = '0'
            elif review_type == "免评":
                record_object.free_review_number = '1'
                record_object.review_number = '0'
                record_object.direct_review = '0'
                record_object.feedback = '0'
            elif review_type == "feedback":
                record_object.free_review_number = '0'
                record_object.review_number = '0'
                record_object.direct_review = '0'
                record_object.feedback = '1'

            record_object.now_score = now_score
            record_object.now_review_number = now_review_number
            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class OperationEditView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = OperationRecordForm(request.POST)
        if form.is_valid():
            record_id = request.POST.get('record_id', '')
            site = request.POST.get('site', '')
            shop = request.POST.get('shop', '')
            product_chinese_name = request.POST.get('product_chinese_name', '')
            sku = request.POST.get('SKU', '')
            order_word = request.POST.get('order_word', '')
            key_word_page_number = request.POST.get('key_word_page_number', '')
            key_word_link = request.POST.get('key_word_link', '')
            order_date = request.POST.get('order_date', '')
            review_date = request.POST.get('review_date', '')

            record_object = Record.objects.get(pk=record_id)
            record_object.site = site
            record_object.shop = shop
            record_object.product_chinese_name = product_chinese_name
            record_object.sku = sku
            record_object.order_word = order_word
            record_object.key_word_page_number = key_word_page_number
            record_object.key_word_link = key_word_link
            record_object.order_date = order_date
            record_object.review_date = review_date

            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


# 刷单修改
class SdBrushEditView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = BrushEditForm(request.POST)
        if form.is_valid():
            record_id = request.POST.get('record_id', '')
            record_object = Record.objects.get(pk=record_id)

            brush_company = request.POST.get('brush_company', '')
            if brush_company:
                brush_company_object = UserProfile.objects.get(pk=brush_company)
                record_object.brush_company = brush_company_object

            order_number = request.POST.get('order_number', '')
            record_object.order_number = order_number

            # 刷单费用
            brush_money = float(request.POST.get('brush_money', 0))
            # 刷单费用的差
            brush_money_difference = brush_money - record_object.brush_money

            # 产品售价
            c_price = 0
            if not record_object.c_price_status:
                price_regex = re.compile("\d+\.?\d+")
                c_price_list = price_regex.findall(record_object.c_price)
                if c_price_list:
                    c_price = float(c_price_list[0])
                    record_object.c_price_status = True

            year = datetime.datetime.now().strftime('%Y')
            month = datetime.datetime.now().strftime('%m')
            user_brush_money = UserBrushMoney.objects.filter(brush_year=year, brush_month=month,
                                                             user=record_object.user).first()
            sum_brush_money = SumBrushMoney.objects.filter(brush_year=year, brush_month=month).first()
            if not sum_brush_money:
                sum_brush_money_object = SumBrushMoney()
            else:
                sum_brush_money_object = sum_brush_money
            sum_brush_money_object.brush_money += round(brush_money_difference, 2)
            sum_brush_money_object.product_cost += round(c_price, 2)
            sum_brush_money_object.save()

            # 如果没有这条记录，先去创建这条记录
            if not user_brush_money:
                user_brush_money_object = UserBrushMoney()
                user_brush_money_object.user = record_object.user
            else:
                user_brush_money_object = user_brush_money
            user_brush_money_object.brush_money += round(brush_money_difference, 2)
            user_brush_money_object.product_cost += round(c_price, 2)
            user_brush_money_object.save()

            record_object.brush_money = brush_money

            review_feedback = request.POST.get('review_feedback', '')
            record_object.review_feedback = review_feedback

            record_status = request.POST.get('record_status', '')
            record_object.record_status = record_status

            record_object.brush_status_three = "already send"

            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class UploadImageView(LoginRequiredMixin, View):
    '''图像修改'''

    def post(self, request):
        # 上传的文件都在request.FILES里面获取，所以这里要多传一个这个参数
        image_form = UploadImageForm(request.POST, request.FILES)
        next_url = request.GET.get('next', '')
        if image_form.is_valid():
            record_id = request.POST.get('record_id', '')
            image = image_form.cleaned_data['main_image']
            record_object = Record.objects.get(pk=record_id)
            record_object.main_image = image
            record_object.save()
            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class DeleteRecordView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')

        record_id = request.POST.get("record_id")
        record_object = Record.objects.get(pk=record_id)
        record_object.delete()
        return redirect(next_url)


# class FavoriteRecordView(LoginRequiredMixin, View):
#     def get(self, request):
#         next_url = request.GET.get('next')
#         id_data = request.GET.get('id_data')
#         record_id_list = [i for i in id_data.split('_') if i != '']
#
#         flag = False
#         for record_id in record_id_list:
#             record_object = Record.objects.get(pk=record_id)
#             if not RecordUser.objects.filter(user=request.user, record=record_object):
#                 record_user = RecordUser()
#                 record_user.record = record_object
#                 record_user.user = request.user
#                 record_user.save()
#                 flag = True
#
#         if flag:
#             messages.add_message(request, messages.SUCCESS, "收藏成功", extra_tags='success')
#         data = {
#             "next_url": next_url
#         }
#         return JsonResponse(data)


class FeedBackFavoriteRecordView(LoginRequiredMixin, View):
    def get(self, request):
        next_url = request.GET.get('next')
        id_data = request.GET.get('id_data')
        record_id_list = [i for i in id_data.split('_') if i != '']

        flag = False
        for record_id in record_id_list:
            record_object = Record.objects.get(pk=record_id)
            if not FeedBackRecordUser.objects.filter(user=request.user, record=record_object):
                record_user = FeedBackRecordUser()
                record_user.record = record_object
                record_user.user = request.user
                record_user.save()
                flag = True

        if flag:
            messages.add_message(request, messages.SUCCESS, "收藏成功", extra_tags='success')
        data = {
            "next_url": next_url
        }
        return JsonResponse(data)
