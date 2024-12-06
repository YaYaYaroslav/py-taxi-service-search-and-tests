from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from taxi.models import Driver, Car, Manufacturer


class SearchTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username="test_driver",
            password="testpass"
        )
        self.client.login(username="test_driver", password="testpass")

        self.manufacturer = Manufacturer.objects.create(
            name="Toyota Manufacturer"
        )
        self.car = Car.objects.create(
            model="Toyota",
            manufacturer=self.manufacturer
        )

    def test_driver_search(self):
        response = self.client.get(reverse("taxi:driver-list") + "?q=test_driver")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_driver")

    def test_car_search(self):
        response = self.client.get(reverse("taxi:car-list") + "?q=Toyota")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toyota")

    def test_manufacturer_search(self):
        response = self.client.get(reverse("taxi:manufacturer-list") + "?q=Toyota")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toyota")
