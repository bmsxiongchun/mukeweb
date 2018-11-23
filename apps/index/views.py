from django.shortcuts import render

# Create your views here.
from django.views import View

from users.models import Banner


class IndexView(View):

    def get(self, request):
        # 首先要取出首页中的轮播图
        all_banners = Banner.objects.all().order_by('index')
        return render(request, 'index.html', {
            'all_banners': all_banners
        })
