from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api$', views.api, name='api'),
    url(r'stddelete$', views.stddelete, name='stddelete'),
    url(r'stdupdate$', views.stdupdate, name='stdupdate'),
    url(r'collect$', views.collect, name='collect')
]