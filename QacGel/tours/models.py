from django.db import models

# Create your models here.
from django.db import models


class TourPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transportation = models.CharField(max_length=50, choices=[('Plane', 'Plane'), ('Bus', 'Bus')])
    duration = models.IntegerField(help_text="Duration in days")
    image = models.ImageField(upload_to='tour_images/')

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title
