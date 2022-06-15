# from django.db import models

# # Create your models here.
from distutils.command.upload import upload
from django.db import models

class image_slider_place(models.Model):
    images = models.ImageField(upload_to='places-visits/', null=True, blank=True)
    def __str__(self) -> str:
        return self.images.url  

# Create your models here.
class Places_visits(models.Model):
    STATUS_CHOICE = (
        ('O','Open'),
        ('C','Closed'),
        ('R', 'Reform'),
    )
    CATEGORY_CHOICE = (
        ('K', 'Kids'),
        ('T', 'Teenager'),
        ('A', 'Adult')
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    description_place = models.TextField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    img = models.ManyToManyField(image_slider_place, null=True, blank=True)
    img_cover = models.ImageField(upload_to='places-visits/cover/', null=True, blank=True)
    operation = models.CharField(help_text='Days of Operation',max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE,  null=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICE, null=True, blank=True)
    favorite = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.name