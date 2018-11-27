from datetime import datetime

from django.db import models

# Create your models here.
from django.db.models import Model, CharField, IntegerField, ImageField, ForeignKey, DateTimeField, CASCADE
from DjangoUeditor.models import UEditorField


class CityDict(Model):
    name = CharField(max_length=20, verbose_name=u'城市')
    desc = CharField(max_length=200, verbose_name=u'描述')
    add_time = DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


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
    add_time = models.DateTimeField(default=datetime.now)
    city = ForeignKey(CityDict, verbose_name=u'所在城市', on_delete=CASCADE)


class Teacher(Model):
    org = ForeignKey(CourseOrg, verbose_name=u'所属机构', on_delete=CASCADE)
    name = CharField(max_length=50, verbose_name=u'教师名')
    work_years = IntegerField(default=0, verbose_name=u'工作年限')
    work_company = CharField(max_length=50, verbose_name=u'就职公司')
    points = CharField(max_length=50, verbose_name=u'教学特点')
    click_nums = IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = IntegerField(default=0, verbose_name=u'收藏数')
    age = IntegerField(default=18, verbose_name=u'年龄')
    image = ImageField(default='', upload_to='teacher/%Y/%m', verbose_name=u'头像', max_length=100)
    add_time = DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_course_count(self):
        return self.course_set.all().count()

