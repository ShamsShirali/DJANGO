from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/<int:id>/', views.tour_detail, name='tour_detail'),
    path('contact/', views.contact, name='contact'),
]
