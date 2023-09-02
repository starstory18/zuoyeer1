from django.db import models


class Teacher(models.Model):
    department = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    photo = models.TextField(max_length=200)

    def __str__(self):
        return "%s,%s,%s,%s\n" % (
            self.department,
            self.name,
            self.title,
            self.photo
        )

# Create your models here.
# 编辑 models.py文件，改变模型
# 运行 python manage.py make migrations myApp 为模型的改变生成迁移文件
# 运行 python manage.py migrate 应用数据库迁移


# python manage.py make migrations myApp
# 创建第一个应用App  .\manage.py startapp myApp
# 启动服务器 python .\manage.py runserver
