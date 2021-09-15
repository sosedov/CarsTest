from django.urls import path, include
from .views import CommonResponseMiddleware


urlpatterns = [
    path ('user/by/token/', CommonResponseMiddleware.as_view()),
]
