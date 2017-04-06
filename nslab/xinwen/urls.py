from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),

    url(r'^titles/$',views.titles,name='titles'),

    url(r'^titles/(\d+)/$',views.title,name='title')
]