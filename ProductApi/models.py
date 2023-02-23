from django.db import models

# Create your models here.

class Product(models.Model):
    ProductName = models.CharField(max_length=400,null=False,blank=False)
    Category = models.CharField(max_length=400,null=False,blank=False)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Description = models.TextField()
    Stars = models.IntegerField()
    
    def __str__(self) -> str:
        return self.ProductName
    

