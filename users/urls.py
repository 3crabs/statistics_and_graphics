from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^$', views.get_users),
    url(r'^(?P<user_id>\d+)$', views.get_one_user),
]