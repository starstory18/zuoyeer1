from django.contrib import admin

from myApp.models import Teacher


# Register your models here.
admin.site.register(Teacher)

#使用createsuperuser命令为管理员注册 python .\manage.py createsuperuser