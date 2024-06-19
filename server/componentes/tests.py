
from django.contrib.auth.models import User
from componentes.models import Equipo, Piloto
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class PilotoTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='123', email='admin@admin.com')
        self.piloto = Piloto.objects.create(nombre = 'Mansel', ingeniero = 'Brown', victoria = 31, años = 14, numero = 5)

    def test_create_piloto(self):
        self.client.login(username='admin', password='123')
        url = '/api/piloto/'
        data = {
            'nombre': 'Mansel',
            'ingeniero': 'Brown',
            'victoria': 31,
            'años': 14,
            'numero':5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_piloto(self):
        self.client.login(username='admin', password='123')
        url = '/api/piloto/'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
        
    
    def test_update_piloto(self):
        self.client.login(username='admin', password='123')
        url = f'/api/piloto/{self.piloto.id}'
        data = {
            'nombre': 'NotMansel',
            'ingeniero': 'Brown',
            'victoria': 31,
            'años': 14,
            'numero':5
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_piloto(self):
        self.client.login(username='admin', password='123')
        url = f'/api/piloto/{self.piloto.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_get_piloto_by_ingeniero(self):
        self.client.login(username='admin', password='123')
        url = '/api/piloto/ingeniero/Brown'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
    
    def test_get_pilotos_con_mas_victorias(self):
        self.client.login(username='admin', password='123')
        url = '/api/piloto/victorias'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
        
class EquipoTestCase(APITestCase):
    
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='123', email='admin@admin.com')
        self.piloto = Piloto.objects.create(nombre = 'Mansel', ingeniero = 'Brown', victoria = 31, años = 14, numero = 5)
        self.equipo = Equipo.objects.create(piloto = self.piloto, nombre = 'Williams', motor = 'Renault')
        
    def test_create_equipo(self):
        self.client.login(username='admin', password='123')
        url = '/api/equipo/'
        data = {
            'piloto': 1,
            'nombre': 'Williams',
            'motor': 'Renault'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_equipo(self):
        self.client.login(username='admin', password='123')
        url = '/api/equipo/'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
        
    def test_update_equipo(self):
        self.client.login(username='admin', password='123')
        url = f'/api/equipo/{self.equipo.id}'
        data = {
            'piloto': self.piloto.id,
            'nombre': 'Ferrari',
            'motor': 'Ferrari'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_equipo(self):
        self.client.login(username='admin', password='123')
        url = f'/api/equipo/{self.equipo.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def get_equipo_by_nombre(self):
        self.client.login(username='admin', password='123')
        url = '/api/equipo/nombre/Williams'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
    
    def get_equipo_by_motor(self):
        self.client.login(username='admin', password='123')
        url = '/api/equipo/motor/Renault'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)


class PilotoByEquipoTestCase(APITestCase):
    
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='123', email='admin@admin.com')
        self.piloto = Piloto.objects.create(nombre = 'Mansel', ingeniero = 'Brown', victoria = 31, años = 14, numero = 5)
        self.equipo = Equipo.objects.create(piloto = self.piloto, nombre = 'Williams', motor = 'Renault')
        
    def test_get_piloto_by_equipo(self):
        self.client.login(username='admin', password='123')
        url = f'/api/piloto/equipo/{self.equipo.id}'
        resposne = self.client.get(url)
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
