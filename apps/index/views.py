from django.shortcuts import render

# Create your views here.
from django.views import View

from courses.models import Course
from organization.models import CourseOrg
from users.models import Banner


class IndexView(View):

    def get(self, request):
        # 首先要取出首页中的轮播图
        all_banners = Banner.objects.all().order_by('index')
        courses = Course.objects.filter(is_banner=False)[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'courses': courses,
            'course_orgs': course_orgs,
            'banner_courses': banner_courses,
        })
