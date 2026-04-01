from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    PRODUCT_STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('out_of_stock', 'Out of Stock')
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='available')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

#one to many relationship 
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Product: {self.product.name} - User: {self.user.username} - Rating: {self.rating}"
    
#many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    product_varieties = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.name
    
#one to one relationship
class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='detail')
    details = models.TextField()

    def __str__(self):
        return f"Details for {self.product.name}" 
