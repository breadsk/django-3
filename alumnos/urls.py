from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    
    path('crud', views.crud, name="crud"),
    path('alumnosAdd', views.alumnosAdd, name="alumnosAdd"),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
    #path('alumnos_add', views.alumnos_add, name="alumnos_add"),
    #path('alumnos_edit', views.alumnos_edit, name="alumnos_edit"),
    #path('alumnos_list', views.alumnos_list, name="alumnos_list"),
]