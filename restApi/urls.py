from django.conf.urls import url
from restApi import views

urlpatterns = [
    url(r'^operadores/$', views.operador_list),
    url(r'^operadores/(?P<pk>[0-9]+)/$', views.operador_detail),
    url(r'^asistencias/$', views.asistencia_list),
    url(r'^asistencias/(?P<pk>[0-9]+)/$', views.asistencia_detail),
]
