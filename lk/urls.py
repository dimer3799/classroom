from django.urls import path
from .views import index

urlpatterns = [
    # post views
    path('index',  index),

]