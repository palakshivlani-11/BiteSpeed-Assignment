from .views import *
from django.urls import path , include

urlpatterns = [
    path('identity/', identity.as_view(), name='identity'),
]