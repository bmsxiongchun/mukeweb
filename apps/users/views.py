from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from users.forms import RegisterForm, LoginForm
from users.models import UsersInfo


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        regist_form = RegisterForm()
        if regist_form.is_valid():
            user_name = request.POST.get("username", "")
            if UsersInfo.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": regist_form, "msg": "用户名已存在"})
            pass_word = request.POST.get("password", "")
            user_info = UsersInfo()
            user_info.username = user_name
            user_info.email = user_name
            user_info.is_active = False
            user_info.password = make_password(password=pass_word)
            user_info.save()

            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": regist_form})


class UserInfoView(View):
    pass


class LogoutView(View):
    # 用户退出登录
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    # 用户登录
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg": "用户未激活!"})
            else:
                return render(request, "login.html", {"msg": "请输入正确的用户名/密码"})
        else:
            return render(request, "login.html", {"login_form": login_form})
