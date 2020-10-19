from django.template import Library

register = Library()  # 必须用register这个变量名


def truncate_word(value):
    # 截断多余字符
    if value:
        if len(value) > 10:
            return value[:10] + '...'
        else:
            return value
    else:
        return value


register.filter(truncate_word)  # 注册convert_male这个过滤器
