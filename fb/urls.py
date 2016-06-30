from django.conf.urls import url
# from django.contrib import admin
from fb import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'start', views.start, name='start'),
    url(r'^check$', views.check, name='check'),
    url(r'^table$', views.table, name='results')
]
