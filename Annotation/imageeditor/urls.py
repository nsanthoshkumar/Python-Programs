'''
Created on Aug 10, 2014

@author: santhosh
'''
from django.conf.urls import patterns, url
from imageeditor import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^index1/$',views.index1, name='index1'),
    url(r'^login/$',views.login, name='login'),
    url(r'^display/$',views.retrieve, name='retrieve'),
    url(r'^(?P<num1>\d+)/(?P<num2>\d+)/$', views.AddTwo, name='AddTwo'),
    url(r'^login/acceptlogin/$',views.acceptlogin, name='acceptlogin'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )