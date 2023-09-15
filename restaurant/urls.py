from django.urls import path
from . import views
from .views import menuView, bookingView, menuItemsView, singleMenuItemView


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
    path('menu/', menuView.as_view()),
]