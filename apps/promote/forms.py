from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['asin', 'content', 'yy_remark']
        error_messages = {
            "asin": {"required": "请输入asin"},
            "content": {"required": "请输入内容"}
        }


class ShProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['company', 'cost', 'sh_remark']
        error_messages = {
            "company": {"required": "请输入公司"},
            "cost": {"required": "请输入费用"}
        }

