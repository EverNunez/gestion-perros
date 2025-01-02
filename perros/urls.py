from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("lista_perros/", views.lista_perros, name="lista_perros"),
    path("agregar_perro/", views.agregar_perro, name="agregar_perro"),
    path("eliminar_perro/<int:perro_id>/", views.eliminar_perro, name="eliminar_perro"),
    path("detalle_perro/<int:perro_id>/", views.detalle_perro, name="detalle_perro"),
    path("agregar_cruce/<int:perro_id>/", views.agregar_cruce, name="agregar_cruce"),
    path("editar_cruce/<int:cruce_id>/", views.editar_cruce, name="editar_cruce"),
    path("eliminar_cruce/<int:cruce_id>/", views.eliminar_cruce, name="eliminar_cruce"),
]

