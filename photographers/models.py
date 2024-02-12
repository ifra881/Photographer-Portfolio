from django.db import models

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default='Your Default Address')
    contact_number = models.CharField(max_length=20, default='Your Default contact')
    email = models.EmailField(default='Your Default email')
    price = models.IntegerField(default='100000')
    class Meta:
        app_label = 'photographers'

class Portfolio(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images')
    
