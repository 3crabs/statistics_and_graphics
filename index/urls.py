from django.conf.urls import url

from index import views

urlpatterns = [
    url(r'^$', views.get_courses),
    url(r'^(?P<course_id>\d+)$', views.get_one_course),
]
