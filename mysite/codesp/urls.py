from django.urls import path
from . import views

app_name = 'codesp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('solicitacao', views.ProfessorView.as_view(), name='solicitacao'),
    path('espacoModalidade', views.BolsistaView.as_view(), name="espacoModalidade"),
    path('autorizarMatricula', views.CodespView.as_view(), name="autorizarMatricula"),
    path('frequencia', views.FrequenciaView.as_view(), name='frequencia'),
]

