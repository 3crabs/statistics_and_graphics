from django.conf.urls import url

from groups import views

urlpatterns = [
    url(r'^$', views.get_groups),
]
