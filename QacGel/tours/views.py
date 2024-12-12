from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import TourPackage, BlogPost

def home(request):
    tours = TourPackage.objects.all()
    return render(request, 'tours/home.html', {'tours': tours})

def tour_detail(request, id):
    tour = get_object_or_404(TourPackage, id=id)
    return render(request, 'tour_detail.html', {'tour': tour})

def contact(request):
    return render(request, 'contact.html')
