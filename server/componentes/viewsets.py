from rest_framework import viewsets

from componentes.models import Piloto
from componentes.serializers import PilotoSerializer

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer