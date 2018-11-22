from users.models import Banner, UsersInfo
from extra_apps import xadmin
from xadmin import views
from xadmin.layout import Main, Fieldset, Row, Side
from xadmin.plugins.auth import UserAdmin
from django.utils.translation import ugettext as _


class BannerAdmin(object):
    list_play = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# class UsersInfoAdmin(UserAdmin):
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()


class GlobalSetting(object):
    site_title = '后台管理系统'
    site_footer = '网站脚本'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.unregister(UsersInfo)
xadmin.site.register(UsersInfo, UserAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
