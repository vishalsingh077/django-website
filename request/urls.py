from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'request'

urlpatterns = [
    #/requests/
    url(r'^requests/$',views.requests_view.as_view() ,name="requests_view"),
 
    #/requests/pk/
    url(r'^requests/(?P<pk>[0-9]+)/$', views.request_detail_view.as_view() ,name = "request_detail_view"),

    #/request/pk/create/
    #url(r'^requests/(?P<pk>[0-9]+)/create/$', views.create_view ,name = "create_view"),

]
