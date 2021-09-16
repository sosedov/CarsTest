from django.urls import path, include
from .views import CarsView


urlpatterns = [
    path ('cars_list', CarsView.as_view()),
    path('cars_list/<int:pk>', CarsView.as_view())
]
