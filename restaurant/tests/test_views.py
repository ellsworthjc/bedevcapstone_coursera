from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):
	def setup(self):
		Menu.objects.create(title="Test Item 1", price=5, inventory=3)
		Menu.objects.create(title="Test Item 2", price=10, inventory=6)
		Menu.objects.create(title="Test Item 3", price=15, inventory=9)

	def test_get_all(self):
		items = []
		items = Menu.objects.all()
		serializer = MenuSerializer(items, many=True)
		self.assertEqual(serializer.data, serializer.data)