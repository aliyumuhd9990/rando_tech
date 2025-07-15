from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='Write Something')
    price1 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    price2 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    price3 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    price4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    price5 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    cover_img = models.ImageField(upload_to='img/post_cover', default='image')
    img1 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    img2 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    img3 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    img4 = models.ImageField(upload_to='img/img', default='img/post_cover/image_1.jpg')
    