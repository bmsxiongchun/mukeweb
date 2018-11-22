from django.urls import path

from courses.views import CourseView
app_name = 'courses'

urlpatterns = [
    path('list/', CourseView.as_view(), name='course_list'),
]