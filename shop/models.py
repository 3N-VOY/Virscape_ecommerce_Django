from django.db import models
from django.template.defaultfilters import slugify  
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='uploads/categories', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url
   
   
 

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    


    class Meta:
        ordering = ('-created_date',)
    def __str__(self):
        return self.title
    
 
    def get_image(self):
        if self.image:
            return self.image.url
   
 
    
    #admin username
    #admin password