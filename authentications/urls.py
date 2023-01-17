
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentications.views import *

urlpatterns = [
    path('user/', UserListView.as_view(), name="user"),
    path('user/<int:pk>/', UserDetailView.as_view(), name="userdet"),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name="userup"),
    path('user/create/', UserCreateView.as_view(), name="usercr"),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name="usdel"),
    path('user/login/', views.obtain_auth_token),
    path('user/logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]