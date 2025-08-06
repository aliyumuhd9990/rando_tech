from django.db import models
from django.urls import reverse

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='Write Something')
    price1 = models.IntegerField(default=0)
    price2 = models.IntegerField(default=0)
    price3 = models.IntegerField(default=0)
    price4 = models.IntegerField(default=0)
    price5 = models.IntegerField(default=0)
    cover_img = models.ImageField(upload_to='img/post_cover', default='image')
    img1 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    img2 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    img3 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    img4 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    
    def get_absolute_url(self):
        return reverse("core:service_detail", kwargs={"id": self.id})
    
    def __str__(self):
        return self.name
class Package(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='packages', default=2)
    name = models.CharField(max_length=50, default='product')
    price = models.IntegerField(default=0)
    
class ContactEmail(models.Model):
    name = models.CharField(max_length=50)
    memail = models.EmailField(max_length=225)
    msg = models.TextField()
    
class Showcase(models.Model):
    work = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='showcase', default=2)
    name = models.CharField(max_length = 50)
    cover_img = models.ImageField(upload_to='img/post_cover')
    link = models.CharField(max_length = 100)
    price = models.IntegerField(default=0)
    
    