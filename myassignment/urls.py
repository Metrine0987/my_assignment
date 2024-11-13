from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The home page URL pattern
    path('service/', views.service_details, name='service-details'),  # Service page URL pattern
    path('portfolio/', views.portfolio_details, name='portfolio-details'),  # Portfolio page URL pattern
    path('starter/', views.starter_page, name='starter-page'),  # Starter page URL pattern
    path('contacts/', views.contacts_page, name ='contacts'),
]
 
