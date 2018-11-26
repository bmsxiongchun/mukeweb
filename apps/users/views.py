from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from users.forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})


class UserInfoView(View):
    pass


class LogoutView(View):
    # 用户退出登录
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reversed('index'))