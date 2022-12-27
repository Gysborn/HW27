from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', CatListView.as_view(), name="catlist"),
    path('cat/<int:pk>/', CatDetailView.as_view(), name="catdet"),
    path('cat/create/', CatCreateView.as_view(), name="catcre"),
    path('cat/update/<int:pk>/', CatUpdateView.as_view(), name="catup"),
    path('cat/delete/<int:pk>/', CatDeleteView.as_view(), name="catdel"),
]