from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views import View
from pure_pagination import Paginator

from courses.models import Course


class CourseView(View):
    def get(self, request):
        pass


class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all().order_by('-add_time')
        hot_course = Course.objects.all().order_by('-click_nums')[:3]

        # 课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_course = all_course.filter(Q(name_icontains=search_keywords)|Q(desc_icontains=search_keywords)|Q(detail_icontains=search_keywords))

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_course = all_course.order_by('-students')
            elif sort == 'hot':
                all_course = all_course.order_by('-click_nums')

        # 对课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course, 12, request=request)

        course = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': course,
            'sort': sort,
            'hot_courses': hot_course,
        })