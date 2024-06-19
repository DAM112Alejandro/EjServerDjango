from rest_framework.views import APIView
from componentes.models import Piloto,Equipo
from componentes.serializers import PilotoSerializer , EquipoSerializer
from rest_framework.response import Response
from rest_framework import generics


##Generica de pilotos
class PilotoListCreate(generics.ListCreateAPIView):
   queryset = Piloto.objects.all()
   serializer_class = PilotoSerializer

        
class PilotoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    
class PilotoByIngeniero(generics.ListAPIView):
    serializer_class = PilotoSerializer
    
    def get_queryset(self):
        ingeniero = self.kwargs['ingeniero']
        return Piloto.objects.filter(ingeniero=ingeniero)

class PilotosConMasVictorias(generics.ListAPIView):
    serializer_class = PilotoSerializer
    
    def get_queryset(self):
        return Piloto.objects.order_by('-victoria') #De mayor a menor
    
#genericas de equipos
class EquipoListCreate(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    
class EquipoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    
class EquipoByNombre(generics.ListAPIView):
    serializer_class = EquipoSerializer
    
    def get_queryset(self):
        nombre = self.kwargs['nombre']
        return Equipo.objects.filter(nombre=nombre)
    
class EquipoByMotor(generics.ListAPIView):
    serializer_class = EquipoSerializer
    
    def get_queryset(self):
        motor = self.kwargs['motor']
        return Equipo.objects.filter(motor=motor)
    

class PilotoByEquipo(APIView):
   def get(self, request,id_Equipo):
        equipo = Equipo.objects.get(id=id_Equipo)
        pilotos = Piloto.objects.filter(equipo=equipo)
        serializer = PilotoSerializer(pilotos, many=True)
        return Response(serializer.data)