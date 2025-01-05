from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Propietarios
    path('',views.inicio),


    path('nuevoEstudiante/', views.nuevoEstudiante),  # Formulario para nuevo estudiante
    path('listadoEstudiante/', views.listadoEstudiante),  # Listado de estudiantes
    path('guardarEstudiante/', views.guardarEstudiante),  # Guardar nuevo estudiante
    path('eliminarEstudiante/<id>/', views.eliminarEstudiante),  # Eliminar estudiante por ID
    path('editarEstudiante/<id>/', views.editarEstudiante),  # Formulario para editar estudiante
    path('procesarEdicionEstudiante/', views.procesarEdicionEstudiante),  # Procesar edición de estudiante

    path('nuevoProfesor/', views.nuevoProfesor),
    path('listadoProfesor/', views.listadoProfesor),
    path('guardarProfesor/', views.guardarProfesor),
    path('eliminarProfesor/<int:id>/', views.eliminarProfesor),
    path('editarProfesor/<int:id>/', views.editarProfesor),
    path('procesarEdicionProfesor/<int:id>/', views.procesarEdicionProfesor),

    # Tarea
    path('nuevaTarea/', views.nuevaTarea),
    path('listadoTarea/', views.listadoTarea),
    path('guardarTarea/', views.guardarTarea),
    path('eliminarTarea/<int:id>/', views.eliminarTarea),
    path('editarTarea/<int:id>/', views.editarTarea),
    path('procesarEdicionTarea/', views.procesarEdicionTarea),


     # Entregas
    path('nuevaEntrega/', views.nuevaEntrega),
     path('listadoEntrega/', views.listadoEntrega),
    path('guardarEntrega/', views.guardarEntrega),
    path('eliminarEntrega/<int:id>/', views.eliminarEntrega),
    path('editarEntrega/<int:id>/', views.editarEntrega),
    path('procesarEdicionEntrega/', views.procesarEdicionEntrega),


  
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
