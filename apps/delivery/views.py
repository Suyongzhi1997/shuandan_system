import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic.base import View
from pure_pagination import Paginator

from delivery.forms import GoodForm
from delivery.models import Goods, UserFreight, LogisticsCompanyFreight
from records.models import Record


class InfosView(LoginRequiredMixin, View):
    def get(self, request):
        title = "物流信息"
        user = request.user
        already_check_records_number = Record.objects.filter(user=request.user,
                                                             brush_status='already check').count() if request.user.username.startswith(
            "yy") else Record.objects.filter(brush_status='already check', audit_results="pass").count()
        feedback_number = Record.objects.filter(user=request.user).filter(~Q(order_number='')).count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()
        # 搜索功能
        search_keywords = request.GET.get('keywords', '')
        search_type = request.GET.get('search_type', '')

        if search_keywords or request.user.username.startswith("sh"):
            all_infos = Goods.objects.all().order_by('-add_time')
        else:
            all_infos = Goods.objects.filter(user=request.user).order_by('-add_time')

        if search_type == 'company':
            all_infos = all_infos.filter(send_company__icontains=search_keywords)
        elif search_type == 'people':
            all_infos = all_infos.filter(
                Q(user__username__icontains=search_keywords) | Q(user__nick_name__icontains=search_keywords))
        elif search_type == "track_number":
            all_infos = all_infos.filter(track_number__icontains=search_keywords)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 这里指从allorg中取五个出来，每页显示5个
        if not search_type:
            p = Paginator(all_infos, 9, request=request)
        else:
            p = Paginator(all_infos, 10000, request=request)
        all_infos = p.page(page)
        html = 'delivery_infos.html' if request.user.username.startswith("yy") else 'delivery_infos_sh.html'
        return render(request, html, {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'feedback_number': feedback_number,
            'title': title,
            'user': user,
            'all_infos': all_infos,
            'search_type': search_type
        })


class AddInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = GoodForm(request.POST)
        if form.is_valid():
            send_time = request.POST.get('send_time', None) if request.POST.get('send_time', None) else None
            send_company = request.POST.get('send_company', None) if request.POST.get('send_company', None) else None
            channel = request.POST.get('channel', None) if request.POST.get('channel', None) else None
            site = request.POST.get('site', None) if request.POST.get('site', None) else None
            country = request.POST.get('country', None) if request.POST.get('country', None) else None
            track_number = request.POST.get('track_number', None) if request.POST.get('track_number', None) else None
            net_weight = request.POST.get('net_weight', None) if request.POST.get('net_weight', None) else None
            volume_weight = request.POST.get('volume_weight', None) if request.POST.get('volume_weight', None) else None
            actual_charged_weight = request.POST.get('actual_charged_weight', None) if request.POST.get(
                'actual_charged_weight', None) else None
            pieces_number = request.POST.get('pieces_number', None) if request.POST.get('pieces_number', None) else None
            includes_price = request.POST.get('includes_price', None) if request.POST.get('includes_price',
                                                                                          None) else None
            other_price = request.POST.get('other_price', None) if request.POST.get('other_price', None) else None
            total_price = request.POST.get('total_price', None) if request.POST.get('total_price', None) else None
            express_time = request.POST.get('express_time', None) if request.POST.get('express_time', None) else None
            express_status = request.POST.get('express_status', None) if request.POST.get('express_status',
                                                                                          None) else None
            settlement = request.POST.get('settlement', None) if request.POST.get('settlement', None) else None
            order_remark = request.POST.get('order_remark', None) if request.POST.get('order_remark', None) else None

            good_object = Goods()
            old_total_price = good_object.total_price if good_object.total_price else 0
            good_object.send_time = send_time
            good_object.send_company = send_company
            good_object.channel = channel
            good_object.site = site
            good_object.user = request.user
            good_object.country = country
            good_object.track_number = track_number
            good_object.net_weight = net_weight
            good_object.volume_weight = volume_weight
            good_object.actual_charged_weight = actual_charged_weight
            good_object.pieces_number = pieces_number
            good_object.includes_price = includes_price
            good_object.other_price = other_price
            good_object.total_price = total_price
            good_object.express_time = express_time
            good_object.express_status = express_status
            good_object.settlement = settlement
            good_object.order_remark = order_remark

            good_object.save()

            year = datetime.datetime.now().strftime('%Y')
            month = datetime.datetime.now().strftime('%m')
            good_total_price = good_object.total_price if good_object.total_price else 0

            user_freight_money = UserFreight.objects.filter(brush_year=year, brush_month=month,
                                                            user=request.user).first()
            total_price_difference = float(good_total_price) - float(old_total_price)
            if not user_freight_money:
                user_freight_money_object = UserFreight()
                user_freight_money_object.user = request.user
            else:
                user_freight_money_object = user_freight_money

            user_freight_money_object.freight += total_price_difference
            user_freight_money_object.save()

            company_freight_money = LogisticsCompanyFreight.objects.filter(brush_year=year, brush_month=month,
                                                                           send_company=send_company).first()
            if not company_freight_money:
                company_freight_money_object = LogisticsCompanyFreight()
                company_freight_money_object.send_company = send_company
            else:
                company_freight_money_object = company_freight_money
            company_freight_money_object.freight += total_price_difference
            company_freight_money_object.save()

            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class EditInfoView(LoginRequiredMixin, View):
    def post(self, request):
        next_url = request.GET.get('next', '')
        form = GoodForm(request.POST)
        if form.is_valid():
            info_id = request.POST.get('info_id', '')
            send_time = request.POST.get('send_time', None) if request.POST.get('send_time', None) else None
            send_company = request.POST.get('send_company', None) if request.POST.get('send_company', None) else None
            channel = request.POST.get('channel', None) if request.POST.get('channel', None) else None
            site = request.POST.get('site', None) if request.POST.get('site', None) else None
            country = request.POST.get('country', None) if request.POST.get('country', None) else None
            track_number = request.POST.get('track_number', None) if request.POST.get('track_number', None) else None
            net_weight = request.POST.get('net_weight', None) if request.POST.get('net_weight', None) else None
            volume_weight = request.POST.get('volume_weight', None) if request.POST.get('volume_weight', None) else None
            actual_charged_weight = request.POST.get('actual_charged_weight', None) if request.POST.get(
                'actual_charged_weight', None) else None
            pieces_number = request.POST.get('pieces_number', None) if request.POST.get('pieces_number', None) else None
            includes_price = request.POST.get('includes_price', None) if request.POST.get('includes_price',
                                                                                          None) else None
            other_price = request.POST.get('other_price', None) if request.POST.get('other_price', None) else None
            total_price = request.POST.get('total_price', None) if request.POST.get('total_price', None) else None
            express_time = request.POST.get('express_time', None) if request.POST.get('express_time', None) else None
            express_status = request.POST.get('express_status', None) if request.POST.get('express_status',
                                                                                          None) else None
            settlement = request.POST.get('settlement', None) if request.POST.get('settlement', None) else None
            order_remark = request.POST.get('order_remark', None) if request.POST.get('order_remark', None) else None

            good_object = Goods.objects.get(pk=info_id)
            old_total_price = good_object.total_price if good_object.total_price else 0
            good_object.send_time = send_time
            good_object.send_company = send_company
            good_object.channel = channel
            good_object.site = site
            good_object.country = country
            good_object.track_number = track_number
            good_object.net_weight = net_weight
            good_object.volume_weight = volume_weight
            good_object.actual_charged_weight = actual_charged_weight
            good_object.pieces_number = pieces_number
            good_object.includes_price = includes_price
            good_object.other_price = other_price
            good_object.total_price = total_price
            good_object.express_time = express_time
            good_object.express_status = express_status
            good_object.settlement = settlement
            good_object.order_remark = order_remark

            good_object.save()

            year = datetime.datetime.now().strftime('%Y')
            month = datetime.datetime.now().strftime('%m')
            good_total_price = good_object.total_price if good_object.total_price else 0

            user_freight_money = UserFreight.objects.filter(brush_year=year, brush_month=month,
                                                            user=request.user).first()
            total_price_difference = float(good_total_price) - float(old_total_price)
            if not user_freight_money:
                user_freight_money_object = UserFreight()
                user_freight_money_object.user = request.user
            else:
                user_freight_money_object = user_freight_money

            user_freight_money_object.freight += total_price_difference
            user_freight_money_object.save()

            company_freight_money = LogisticsCompanyFreight.objects.filter(brush_year=year, brush_month=month,
                                                                           send_company=send_company).first()
            if not company_freight_money:
                company_freight_money_object = LogisticsCompanyFreight()
                company_freight_money_object.send_company = send_company
            else:
                company_freight_money_object = company_freight_money
            company_freight_money_object.freight += total_price_difference
            company_freight_money_object.save()

            return redirect(next_url)
        else:
            messages.add_message(request, messages.ERROR, "表单验证错误", extra_tags='danger')
            return redirect(next_url)


class DeleteInfoView(LoginRequiredMixin, View):
    def get(self, request):
        next_url = request.GET.get('next')
        id_data = request.GET.get('id_data')
        id_list = [i for i in id_data.split('_') if i != '']

        flag = False
        for g_id in id_list:
            good_object = Goods.objects.filter(pk=g_id, user=request.user).first()

            if good_object:
                flag = True
                year = datetime.datetime.now().strftime('%Y')
                month = datetime.datetime.now().strftime('%m')
                good_total_price = good_object.total_price if good_object.total_price else 0

                user_freight_money = UserFreight.objects.filter(brush_year=year, brush_month=month,
                                                                user=request.user).first()
                total_price_difference = float(good_total_price)
                if user_freight_money:
                    user_freight_money_object = user_freight_money

                    user_freight_money_object.freight -= total_price_difference
                    user_freight_money_object.save()

                company_freight_money = LogisticsCompanyFreight.objects.filter(brush_year=year, brush_month=month,
                                                                               send_company=good_object.send_company).first()
                if company_freight_money:
                    company_freight_money_object = company_freight_money
                    company_freight_money_object.freight -= total_price_difference
                    company_freight_money_object.save()
                good_object.delete()

        if flag:
            messages.add_message(request, messages.SUCCESS, "删除物流信息成功", extra_tags='danger')
        data = {
            "next_url": next_url
        }
        return JsonResponse(data)


class UserFreightView(LoginRequiredMixin, View):
    def get(self, request):
        title = "运营运费"
        user = request.user
        brush_moneys = UserFreight.objects.all().order_by('-add_time')
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()

        return render(request, 'sh_freight_money.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'brush_moneys': brush_moneys
        })


class CompanyFreightView(LoginRequiredMixin, View):
    def get(self, request):
        title = "刷单公司运费"
        user = request.user
        brush_moneys = LogisticsCompanyFreight.objects.all().order_by('-add_time')
        already_check_records_number = Record.objects.filter(brush_status='already check', audit_results="pass").count()
        already_brush_records_number = Record.objects.filter(brush_status_three='already send').count()

        return render(request, 'company_freight.html', {
            'already_check_records_number': already_check_records_number,
            'already_brush_records_number': already_brush_records_number,
            'title': title,
            'user': user,
            'brush_moneys': brush_moneys
        })
