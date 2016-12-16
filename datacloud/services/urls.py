from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api$', views.api, name='api'),
    url(r'addBatch$', views.addBatch, name='addBatch'),
    url(r'updateBatch$', views.updateBatch, name='updateBatch'),
    url(r'deleteBatch$', views.deleteBatch, name='deleteBatch'),
    url(r'getBatchNames$', views.getBatchNames, name='getBatchNames'),
    url(r'stddelete$', views.stddelete, name='stddelete'),
    url(r'stdupdate$', views.stdupdate, name='stdupdate'),
    url(r'collect$', views.collect, name='collect'),
    url(r'studentFee$', views.studentFee, name='studentFee')
]