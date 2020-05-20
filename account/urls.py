from django.urls import path
from .views import index, registration

urlpatterns = [
    # post views
    path('login/',  index),
    path('sign_in/',  registration),
    #path('sign_in/',  user_login, name='registration'),
    path('',  index),
]