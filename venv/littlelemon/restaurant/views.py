from django.shortcuts import render

# Create your views here.
def index(request):
 return render(request, 'index.html', {})


# restaurant/views.py
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
