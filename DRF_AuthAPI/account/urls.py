from django.urls import path , include
from account.views import UserRegistration

urlpatterns = [
    path('register/', UserRegistration.as_view(),name='register')
]
