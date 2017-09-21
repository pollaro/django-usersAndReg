from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$',views.index,name='index'),
    url(r'^login/register$',views.register,name='register'),
    url(r'^login/login$',views.login,name='login'),
    url(r'^login/success/(?P<id>[0-9]{1,})',views.success,name='success')
]
