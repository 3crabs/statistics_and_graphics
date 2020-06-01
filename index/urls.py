from django.conf.urls import url

from index import views

urlpatterns = [
    url(r'^$', views.get_courses),
    url(r'^(?P<course_id>\d+)$', views.get_one_course),
    url(r'^(?P<course_id>\d+)/download$', views.download_one_course),
    url(r'^(?P<course_id>\d+)/save$', views.save_one_course),
    url(r'^(?P<course_id>\d+)/users/(?P<user_id>\d+)$', views.get_course_one_user),
    url(r'^(?P<course_id>\d+)/users/(?P<user_id>\d+)/save$', views.save_course_one_user),
    url(r'^(?P<course_id>\d+)/users/(?P<user_id>\d+)/download$', views.download_course_one_user),
]
