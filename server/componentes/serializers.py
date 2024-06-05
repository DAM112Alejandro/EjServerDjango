from rest_framework import serializers
from models import Piloto , Equipo

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        field = ['id','nombre','ingeniero','victoria','años','numero']

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        field = ['id','piloto','nombre','motor']
        

         