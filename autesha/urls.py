from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.staff_list, name='staff_list'),
]
