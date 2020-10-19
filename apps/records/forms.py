from django import forms

from .models import Record


class OperationRecordForm(forms.Form):
    site = forms.CharField(max_length=100)
    shop = forms.CharField(max_length=100)
    product_chinese_name = forms.CharField(max_length=100)
    SKU = forms.CharField(max_length=100)
    order_word = forms.CharField(max_length=100)
    key_word_link = forms.CharField(max_length=2000)
    key_word_page_number = forms.CharField(max_length=100)
    order_date = forms.DateField()
    review_date = forms.DateField()


class BrushEditForm(forms.Form):
    brush_company = forms.CharField(max_length=100, required=False)
    order_number = forms.CharField(max_length=100, required=False)
    brush_money = forms.FloatField(required=False)
    review_feedback = forms.CharField(max_length=100, required=False)


class SdgsBrushEditForm(forms.Form):
    order_number = forms.CharField(max_length=100, required=False)
    # operating_cost = forms.FloatField(required=False)
    brush_money = forms.FloatField(required=False)
    review_feedback = forms.CharField(max_length=1000, required=False)


class CheckRecordForm(forms.Form):
    ASIN = forms.CharField(max_length=100)
    c_price = forms.CharField(max_length=100)
    purchase_cost = forms.FloatField(min_value=0)
    product_profit = forms.FloatField(min_value=0)
    product_upload_time = forms.DateTimeField()
    # brush_number = forms.IntegerField()
    sale_30_number = forms.IntegerField()
    sale_7_number = forms.IntegerField()
    record_src = forms.CharField(max_length=1000)
    review_type = forms.CharField(max_length=100)
    now_score = forms.CharField(max_length=100)
    now_review_number = forms.IntegerField()


class UploadImageForm(forms.ModelForm):
    '''产品更改图像'''

    class Meta:
        model = Record
        fields = ['main_image']


class DirectReviewForm(forms.Form):
    direct_review_title = forms.CharField(max_length=1000)
    direct_review_content = forms.Textarea()
    direct_review_remark = forms.CharField(max_length=1000, required=False)
