"""
Testes unitários para o app persons.

Este módulo contém testes completos para modelos, formulários, views e
validações do app persons.
"""

from datetime import date, timedelta
from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError

from .models import State, City, Address


# ================================Testes para o modelo State================================
class StateModelTest(TestCase):
    def setUp(self):
        self.state = State.objects.create(name="São Paulo", abbreviation="SP")

    def test_state_creation(self):
        self.assertEqual(self.state.name, "São Paulo")
        self.assertEqual(self.state.abbreviation, "SP")

    def test_state_str_representation(self):
        self.assertEqual(str(self.state), "SP (São Paulo)")

    def test_state_ordering(self):
        state2 = State.objects.create(name="Rio de Janeiro", abbreviation="RJ")
        states = State.objects.all()
        self.assertEqual(states[0], state2)
        self.assertEqual(states[1], self.state)
    
# ===============================Testes para o modelo City================================
class CityModelTest(TestCase):
    def setUp(self):
        self.state = State.objects.create(name="São Paulo", abbreviation="SP")
        self.city = City.objects.create(name="São Paulo", state=self.state)

    def test_city_creation(self):
        self.assertEqual(self.city.name, "São Paulo")
        self.assertEqual(self.city.state, self.state)

    def test_city_str_representation(self):
        self.assertEqual(str(self.city), "São Paulo - SP")

    def test_city_ordering(self):
        city2 = City.objects.create(name="Campinas", state=self.state)
        cities = City.objects.all()
        self.assertEqual(cities[0], city2)
        self.assertEqual(cities[1], self.city)

# ==============================Testes para o modelo Address================================
class AddressModelTest(TestCase):
    
    def setUp(self):
        self.state = State.objects.create(name="São Paulo", abbreviation="SP")
        self.city = City.objects.create(name="São Paulo", state=self.state)
        self.address = Address.objects.create(
            street_suffix="Rua",
            street_name="das Flores",
            neighborhood="Jardim das Acácias",
            city=self.city,
            zip_code="01000-000"
        )

    def test_address_creation(self):
        self.assertEqual(self.address.street_suffix, "Rua")
        self.assertEqual(self.address.street_name, "das Flores")
        self.assertEqual(self.address.neighborhood, "Jardim das Acácias")
        self.assertEqual(self.address.city, self.city)
        self.assertEqual(self.address.zip_code, "01000-000")

    def test_address_str_representation(self):
        expected_str = "01000-000 - Rua das Flores - Jardim das Acácias, São Paulo - SP"
        self.assertEqual(str(self.address), expected_str)

    def test_address_ordering(self):
        address_2 = Address.objects.create(
            street_suffix="Avenida",
            street_name="Paulista",
            neighborhood="Bela Vista",
            city=self.city,
            zip_code="01310-100"
        )
        addresses = Address.objects.all()

        self.assertEqual(addresses[0], address_2)
        self.assertEqual(addresses[1], self.address)
