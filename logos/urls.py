from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'logos'

urlpatterns = [
    #home
    url(r'^$', views.home_view ,name ="home_view"),
    
    #/logos/
    url(r'^logos/$', views.logos_view , name = "logos_view"),

    #/logos/pk/
    url(r'^logos/(?P<pk>[0-9]+)/$', views.logo_detail_view ,name = "logo_detail_view"),

    #/logos/download/pk/
    url(r'^logos/download/(?P<pk>[0-9]+)/$', views.logo_download_view ,name = "logo_download_view"),

    

]
