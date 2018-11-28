from django.urls import path

from courses.views import CourseView, CourseListView

app_name = 'courses'

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name='course_list'),
    path(r'^detail/(?P<course_id>\d+)/$', CourseView.as_view(), name='course_detail'),
]