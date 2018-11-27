"""mukeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve

import xadmin
from django.urls import path, include

from index.views import IndexView
from mukeweb import settings
from mukeweb.settings import MEDIA_ROOT
from users.views import RegisterView, LogoutView, LoginView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('courses/', include(('courses.urls', 'courses'), namespace='course')),
    path('org/', include(('organization.urls', 'organization'), namespace='org')),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('captcha/', include('captcha.urls')),
    # path(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    path(r'forget_pwd/', IndexView.as_view(), name='forget_pwd'),
    path('', IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

