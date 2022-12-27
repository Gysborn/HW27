
from django.urls import path

from .views import *

urlpatterns = [
    path('user/', UserListView.as_view(), name="user"),
    path('user/<int:pk>/', UserDetailView.as_view(), name="userdet"),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name="userup"),
    path('user/create/', UserCreateView.as_view(), name="usercr"),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name="usdel"),
]