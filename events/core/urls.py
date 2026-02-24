from django.urls import path
from .import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_details, name='event_details'),
    path('register-event/<int:pk>/', views.register_event, name='register_event'),
    path('my-events/', views.my_events, name='my_events'),
    path('register/', views.register, name='register'),
]