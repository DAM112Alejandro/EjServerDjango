from django.urls import path
from views import PilotoListCreate,PilotoRetrieveUpdateDestroy,PilotoByIngeniero,PilotosConMasVictorias,EquipoListCreate,EquipoRetrieveUpdateDestroy,EquipoByNombre,EquipoByMotor,PilotoByEquipo

urlpatterns = [
    path ('piloto/',PilotoListCreate.as_view(), name='piloto_list_create'),
    path ('piloto/<int:pk>',PilotoRetrieveUpdateDestroy.as_view(), name='piloto_retrieve_update_destroy'),
    path ('piloto/ingeniero/<str:ingeniero>',PilotoByIngeniero.as_view(), name='piloto_by_ingeniero'),
    path ('piloto/victorias/<int:victorias>',PilotosConMasVictorias.as_view() , name='pilotos_victorias'),
    
    path ('equipo/',EquipoListCreate.as_view(), name='equipo_list_create'),
    path ('equipo/<int:pk>',EquipoRetrieveUpdateDestroy.as_view(), name='Equipo_retrieve_update_destroy'),
    path ('equipo/<str:nombre>',EquipoByNombre.as_view(), name='EquipoByNombre'),
    path ('equipo/motor/<str:motor>', EquipoByMotor.as_view(), name='CocheByMotor'),
    
    path ('piloto/equipo/<int:id_Equipo>', PilotoByEquipo.as_view(),name='piloto_by_equipo')
]
