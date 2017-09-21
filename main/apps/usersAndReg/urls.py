from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register',views.regiester,name='register')
    url(r'^login',views.login,name='login')
    url(r'^success',views.success,name='success')
]
