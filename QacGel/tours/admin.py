from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TourPackage, BlogPost

admin.site.register(TourPackage)
admin.site.register(BlogPost)
