from django.urls import path
from . import views

app_name = 'photographers'  # Namespace for the app

urlpatterns = [
    path('', views.photographer_list, name='photographer_list'),
    path('portfolio/<int:photographer_id>/', views.portfolio_detail, name='portfolio_detail'),    # Add other URL patterns as needed
]
