from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Menu  # Replace 'yourapp' with the actual name of your app

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        item1 = Menu()
        item1.Title = "IceCream"
        item1.Price = 80
        item1.Inventory=100
        
        item2 = Menu()
        item2.Title = "Pizza"
        item2.Price = 20
        item2.Inventory=110
        
        
        #Menu.objects.create(item1)
        #Menu.objects.create(item2)


    def test_getall(self):
        # Retrieve all Menu objects
        # url = reverse('restaurant:MenuItemsView')  # Replace 'menu-list' with the actual URL name for your view
        # client = APIClient()
        # response = client.get(url)
        serialized_data = [
            {'title': 'IceCream', 'price': '80', 'inventory': '100'},
            {'title': 'Pizza', 'price': '20', 'inventory': '110'}
        ]

        # Check if the response status code is 200 (OK)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # # Serialize the retrieved data
        # serialized_data = response.data

        # Assert that the serialized data matches the expected data
        expected_data = [
            {'title': 'IceCream', 'price': '80', 'inventory': '100'},
            {'title': 'Pizza', 'price': '20', 'inventory': '110'}
        ]
        self.assertEqual(serialized_data, expected_data)