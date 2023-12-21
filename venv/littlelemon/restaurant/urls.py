#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('tables/', include(router.urls)),
]