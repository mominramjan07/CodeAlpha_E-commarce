from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    # session-based cart: session_key identifies the visitor
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Order(models.Model):
    # Simple order: stores basic billing/customer info and total
    name = models.CharField(max_length=200)            # customer name
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
                                                ('Pending', 'Pending'),
                                                ('Approved', 'Approved'), 
                                                ('Shipped', 'Shipped'),
                                                 ('Delivered', 'Delivered')], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order {self.id} - {self.name} ({self.status})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
class Laptop(models.Model):
         name = models.CharField(max_length=200)
         slug = models.SlugField(unique=True)
         description = models.TextField(blank=True)
         price = models.DecimalField(max_digits=10, decimal_places=2)
         image = models.ImageField(upload_to="laptops/", blank=True, null=True)
         created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name

class Watch(models.Model):
         name = models.CharField(max_length=200)
         slug = models.SlugField(unique=True)
         description = models.TextField(blank=True)
         price = models.DecimalField(max_digits=10, decimal_places=2)
         image = models.ImageField(upload_to="Watchs/", blank=True, null=True)
         created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name

class Mobile(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="Mobiles/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name
    
class Book(models.Model):
     name = models.CharField(max_length=200)
     slug = models.SlugField(unique=True)
     description = models.TextField(blank=True)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to="Books/", blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name
    
class Clothing(models.Model):
       name = models.CharField(max_length=200)
       slug = models.SlugField(unique=True)
       description = models.TextField(blank=True)
       price = models.DecimalField(max_digits=10, decimal_places=2)
       image = models.ImageField(upload_to="Clothings/", blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name

