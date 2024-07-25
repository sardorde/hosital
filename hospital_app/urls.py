from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('index/', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('service/', views.service_view, name='service'),
    path('team/', views.team_view, name='team'),
    path('feature/', views.feature_view, name='feature'),
    path('appointment/', views.appointment_view, name='appointment'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
    path('eror/', views.eror_404_view, name='eror'),
]
