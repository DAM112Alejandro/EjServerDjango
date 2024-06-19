from rest_framework.routers import DefaultRouter
from componentes.viewsets import PilotoViewSet

router = DefaultRouter()

router.register('pilotos', PilotoViewSet , basename='pilotos')
urlpatterns = router.urls