from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restApi import views, reporte

urlpatterns = [
    url(r'^operadores/$', views.OperadorList.as_view()),
    url(r'^operadores/(?P<pk>[0-9]+)/$', views.OperadorDetail.as_view()),
    url(r'^asistencias/$', views.AsistenciaList.as_view()),
    url(r'^asistencias/(?P<pk>[0-9]+)/$', views.AsistenciaDetail.as_view()),
    url(r'^admins/$', views.AdminList.as_view()),
    url(r'^enviar_reporte/', reporte.EnviarReporte.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
