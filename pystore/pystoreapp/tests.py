from django.test import TestCase

from pystoreapp.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Milk", description="Cow milk", price=10.0, status=1)
        Product.objects.create(name="Bread", description="White bread", price=1.0, status=0)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        milk = Product.objects.get(name="Milk")
        bread = Product.objects.get(name="Bread")
        self.assertEqual(milk.getPrice(), 10.0)
        self.assertEqual(bread.getPrice(), 1.0)