"""
    user route 
"""

from django.urls import path
from .views import UserCreateView, UserRetrieveUpdateDeleteView, UserListView


urlpatterns = [
    path('user/', UserCreateView.as_view(), name='create_user'),
    path('users/', UserListView.as_view(), name='list_users'),
    path('user/<str:pk>/', UserRetrieveUpdateDeleteView.as_view(), 
         name='user_detail'),

] 