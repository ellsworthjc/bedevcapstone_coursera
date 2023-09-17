from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):
	def test_get_item(self):
		item = Menu.objects.create(title="Test Item", price=15, inventory=9)
		self.assertEqual(str(item), "Test Item : 15")