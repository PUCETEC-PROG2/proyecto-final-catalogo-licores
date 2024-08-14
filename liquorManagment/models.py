from django.utils import timezone
from django.db import models

# Create your models here.

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    category_name = models.CharField(null=False, max_length=250)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    id_product= models.AutoField(primary_key=True)
    product_name= models.CharField(null=False, max_length=250)
    price= models.DecimalField(null=False,max_digits=10, decimal_places=2, default=0.00)
    product_image= models.ImageField(upload_to='product_images/')
    created_at= models.DateTimeField(auto_now_add=True)
    is_active= models.BooleanField(null=False)
    available_stock= models.IntegerField(null=False)
    Category_id_fk = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    identification = models.BigIntegerField(unique=True, null=False)
    name = models.CharField(null=False, max_length=250)
    last_name = models.CharField(null=False, max_length=250)
    phone = models.BigIntegerField(null=False)
    email = models.EmailField(max_length=250, null=False)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Purchase_order(models.Model):
    id_purchase_order = models.AutoField(primary_key=True)
    id_client_fk = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_purchase_order
    

class Order_item(models.Model):
    purchase_order_id_fk = models.ForeignKey(Purchase_order, on_delete=models.CASCADE)
    product_id_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f'{self.product_id_fk} - {self.quantity}'
    