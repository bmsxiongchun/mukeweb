from django.db import models

# Create your models here.
from django.db.models import Model, CharField, IntegerField, ImageField
from DjangoUeditor.models import UEditorField

class CourseOrg(Model):
    name = CharField(max_length=50, verbose_name=u'机构名称')
    desc = UEditorField(verbose_name=u'机构描述', width=900, height=300, imagePath='org/ueditor/',
                        filePath='org/ueditor/', default='')
    tag = CharField(default=u'全国知名', max_length=10, verbose_name=u'机构标签')
    category = CharField(default='pxjg', verbose_name=u'机构类别', max_length=20, choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')))
    click_nums = IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = IntegerField(default=0, verbose_name=u'收藏数')
    image = ImageField(upload_to='org/%Y/%m', verbose_name=u'logo', max_length=100)
    address = CharField(max_length=150, verbose_name=u'地址')
    students = IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = IntegerField(default=0, verbose_name=u'学习人数')
