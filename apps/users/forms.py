from django import forms


# 登录表单
class LoginForm(forms.Form):
    # 用户密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
