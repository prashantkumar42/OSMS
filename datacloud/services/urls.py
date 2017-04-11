from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'search$', views.search, name='search'),
    url(r'api$', views.api, name='api'),
    url(r'addBatch$', views.addBatch, name='addBatch'),
    url(r'updateBatch$', views.updateBatch, name='updateBatch'),
    url(r'deleteBatch$', views.deleteBatch, name='deleteBatch'),
    url(r'getBatchNames$', views.getBatchNames, name='getBatchNames'),
    url(r'stddelete$', views.stddelete, name='stddelete'),
    url(r'stdupdate$', views.stdupdate, name='stdupdate'),
    url(r'collect$', views.collect, name='collect'),
    url(r'studentFee$', views.studentFee, name='studentFee'),
    url(r'addCourse$', views.addCourse, name='addCourse'),
    url(r'getCourses$', views.getCourses, name='getCourses'),
    url(r'deleteCourse$', views.deleteCourse, name='deleteCourse'),
    url(r'addGrades$', views.addGrades, name='addGrades'),
    url(r'getGrades$', views.getGrades, name='getGrades'),
    url(r'getFee$', views.getFee, name='getFee'),
    url(r'chartNumStudents$', views.getChartNumStudents, name="chartNumStudents")
]