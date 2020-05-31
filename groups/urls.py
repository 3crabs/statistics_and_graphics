from django.conf.urls import url

from groups import views

urlpatterns = [
    url(r'^$', views.get_groups),
    url(r'^(?P<group_id>\d+)$', views.get_one_group),
]