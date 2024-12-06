from django.test import TestCase
from django.urls import reverse
from taxi.models import Driver, Car, Manufacturer


class SearchTests(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create_user(
            username="test_driver",
            password="password123"
        )

        self.manufacturer = Manufacturer.objects.create(name="Toyota Manufacturer")
        self.car = Car.objects.create(model="Toyota", manufacturer=self.manufacturer)

    def test_driver_search(self):
        response = (
            self.client.get(reverse("taxi:driver-list") + "?q=test_driver")
        )
        self.assertContains(response, "test_driver")

    def test_car_search(self):
        response = self.client.get(reverse("taxi:car-list") + "?q=Toyota")
        self.assertContains(response, "Toyota")

    def test_manufacturer_search(self):
        response = (
            self.client.get(reverse("taxi:manufacturer-list") + "?q=Toyota")
        )
        self.assertContains(response, "Toyota")
