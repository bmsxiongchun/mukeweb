from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DateField, ImageField, URLField, IntegerField, DateTimeField


class UsersInfo(AbstractUser):
    nick_name = CharField(max_length=50, verbose_name=u'昵称', default=u'')
    birthday = DateField(verbose_name=u'生日', null=True, blank=True)
    gender = CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default=u'male', verbose_name=u'性别')
    address = CharField(max_length=100, default=u'', verbose_name=u'地址')
    mobile = CharField(max_length=20, null=True, blank=True, verbose_name=u'手机')
    image = ImageField(upload_to='image/%Y/%m', default=u'image/default.png')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Banner(Model):
    title = CharField(max_length=100, verbose_name=u'标题')
    image = ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图')
    url = URLField(max_length=200, verbose_name=u'访问地址')
    index = IntegerField(default=100, verbose_name=u'访问顺序')
    add_time = DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
