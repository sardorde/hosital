from django.shortcuts import render

# Create your views here.

def eror_404_view(request):
     return render(request, '404.html')

def about_view(request):
     return render(request, 'about.html')

def appointment_view(request):
     return render(request, 'appointment.html')

def contact_view(request):
     return render(request, 'contact.html')

def feature_view(request):
     return render(request, 'feature.html')

def index_view(request):
     return render(request, 'index.html')

def service_view(request):
     return render(request, 'service.html')

def team_view(request):
     return render(request, 'team.html')     

def testimonial_view(request):
     return render(request, 'testimonail.html')     