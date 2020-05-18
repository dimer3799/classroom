from django.urls import path
from .views import user_login, index

urlpatterns = [
    # post views
    path('login/',  index, name='index'),
    path('sign_in/',  user_login, name='sign_in'),
    path('',  index, name='index'),
]