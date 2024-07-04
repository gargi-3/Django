from django.test import TestCase
from .models import Item

# Create your tests here.
class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Test Item", description="Test Description")

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        # self.assertEqual(self.item.description, "Test Description")
        self.assertEqual(self.item.description, "Test Description for item")