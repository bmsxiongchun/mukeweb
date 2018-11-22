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
import xadmin
from django.urls import path, include

from index.views import IndexView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('register/', IndexView.as_view, name='register'),
    path('login/', IndexView.as_view, name='login'),
    path('^courses/', include(('courses.urls', 'courses'), namespace='course')),
    path('^org/', include(('organization.urls', 'organization'), namespace='org')),
    path('', IndexView.as_view(), name='index'),
]
