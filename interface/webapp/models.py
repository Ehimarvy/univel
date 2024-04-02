from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=50)
    supply_price=models.DecimalField(max_digits=20, decimal_places=2)
    selling_price=models.DecimalField(max_digits=20, decimal_places=2)
    supply_date=models.DateField()
    stock_amt=models.PositiveBigIntegerField()
    thumbnail=models.ImageField(upload_to="products")
    brand=models.CharField(max_length=50)

def _str_(self) -> str:
        return f"{self.name}"
