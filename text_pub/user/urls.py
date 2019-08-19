"""
    file:user/urls.py
    路由解析"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reg$',views.reg_view),
    url(r'^login$',views.login_view),
    url(r'^logout$',views.logout_view),
]