#coding=utf8
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.recipe_list),
    url(r'^ajax/$', views.ajax),
    # url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
    # url(r'^recipe/(?P<pk>[0-9]+)/edit/$', views.recipe_edit, name='recipe_edit'),
)