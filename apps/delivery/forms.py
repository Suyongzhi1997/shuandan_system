from django import forms

from .models import Goods


class GoodForm(forms.Form):
    send_time = forms.DateTimeField(required=False)
    send_company = forms.CharField(max_length=100, required=False)
    channel = forms.CharField(max_length=100, required=False)
    site = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=False)
    track_number = forms.CharField(max_length=100, required=False)
    net_weight = forms.CharField(max_length=100, required=False)
    volume_weight = forms.CharField(max_length=100, required=False)
    actual_charged_weight = forms.CharField(max_length=100, required=False)
    pieces_number = forms.CharField(max_length=100, required=False)
    includes_price = forms.CharField(max_length=100, required=False)
    other_price = forms.CharField(max_length=100, required=False)
    total_price = forms.CharField(max_length=100, required=False)
    express_time = forms.DateTimeField(required=False)
    express_status = forms.CharField(max_length=100)
    settlement = forms.CharField(max_length=100, required=False)
    order_remark = forms.CharField(max_length=100, required=False)
