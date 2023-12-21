from django.test import TestCase
from ..models import Menu  # Replace 'yourapp' with the actual name of your app

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu()
        item.Title = "IceCream"
        item.Price = 80
        item.Inventory=100
        #item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")