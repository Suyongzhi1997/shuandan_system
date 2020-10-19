from django import forms
from django.forms import ModelForm

from .models import File


class UploadExcelForm(forms.ModelForm):
    '''产品更改图像'''

    class Meta:
        model = File
        fields = ['excel_file']