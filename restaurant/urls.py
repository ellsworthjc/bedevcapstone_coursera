from django.urls import path
from . import views
from .views import menuView, bookingView, menuItemsView, singleMenuItemView, BookingViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    # path('menu/', views.menu, name="menu"),
    # path('bookings', views.bookings, name='bookings'),
    path('booking/', bookingView.as_view()),
    path('menu/', menuItemsView.as_view()),
    path('menu/<int:pk>', singleMenuItemView.as_view()),
    path('api-token-auth', obtain_auth_token),
]