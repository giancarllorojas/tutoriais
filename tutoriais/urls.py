"""
Arquivo de configuração de URL para o APP de tutoriais
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tutoriais/(?P<categoria_id>[-\w]+)', views.lista_tutoriais_categoria, name='Lista de tutoriais na categoria'),
    url(r'^tutoriais/', views.lista_tutoriais, name='Lista de tutoriais'),
    url(r'^tutorial/(?P<tutorial_id>[-\w]+)/(?P<artigo_id>[-\w]+)', views.ver_artigo, name='Artigo'),
    url(r'^tutorial/(?P<tutorial_id>[-\w]+)', views.ver_tutorial, name='Tutorial')
]