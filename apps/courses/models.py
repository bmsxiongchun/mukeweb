from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.
from django.db.models import Model, ForeignKey, CharField, BooleanField, IntegerField, ImageField, DateTimeField, \
    CASCADE

from organization.models import CourseOrg, Teacher


class Course(Model):
     course_org = ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True, on_delete=CASCADE)
     name = CharField(max_length=50, verbose_name=u'课程名')
     desc = CharField(max_length=300, verbose_name=u'课程描述')
     detail = UEditorField(verbose_name=u'课程详情', width=600, height=300, imagePath='course/ueditor/', filePath='course/ueditor/', default='')
     is_banner = BooleanField(default=False, verbose_name=u'是否轮播')
     teacher = ForeignKey(Teacher, verbose_name=u'讲师', null=True, blank=True, on_delete=CASCADE)
     degree = CharField(max_length=2, verbose_name=u'难度', choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")))
     learn_times = IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
     students = IntegerField(default=0, verbose_name=u'学习人数')
     fav_nums = IntegerField(default=0, verbose_name=u'收藏人数')
     image = ImageField(upload_to='course/%Y/%m', verbose_name=u'封面图', max_length=100)
     click_nums = IntegerField(default=0, verbose_name=u'点击数')
     category = CharField(default=u'后端开发', max_length=20, verbose_name=u'课程类别')
     tag = CharField(default='', verbose_name=u'课程标签', max_length=10)
     youneed_know = CharField(default='', max_length=300, verbose_name=u'课程须知')
     teacher_tell = CharField(default='', max_length=300, verbose_name=u'老师告诉你')
     add_time = DateTimeField(default=datetime.now(), verbose_name=u'添加时间')

     class Meta:
         verbose_name = u'课程'
         verbose_name_plural = verbose_name
