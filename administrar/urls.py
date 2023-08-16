
from django.urls import path

from .views import v_index, v_eliminar, v_completado, v_logout, v_login

 
urlpatterns = [

  path('', v_index),
  path('cerrar-sesion',v_logout),
  path('Iniciar-sesion',v_login),
  path('tarea/<int:tarea_id>/eliminar',v_eliminar),
  path('tarea/<int:tarea_id>/completado',v_completado),
  
  
  
]