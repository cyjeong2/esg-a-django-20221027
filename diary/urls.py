from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.memory_detail),
    path('', views.index)
]