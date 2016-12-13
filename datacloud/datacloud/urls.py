from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^services/', include('services.urls'))
]
