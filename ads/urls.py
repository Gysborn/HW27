from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('ad/', AdListView.as_view(), name="adlist"),
    path('ad/<int:pk>/', AdDetailView.as_view(), name="addet"),
    path('ad/create/', AdCreateView.as_view(), name="ad"),
    path('ad/delete/<int:pk>/', AdDeleteView.as_view(), name="addel"),
    path('ad/update/<int:pk>/', AdUpdateView.as_view(), name="adup"),
    path('ad/<int:pk>/upload_image/', AdUploadImage.as_view(), name="upimage"),
]