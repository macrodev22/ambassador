from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_ambassador = False
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a passpord')
        
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_ambassador = False
        user.save(using=self._db)

        return user

class User(AbstractUser):
    username = None # Remove username field
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=500)
    is_ambassador = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def revenue(self):
        # get orders for the user
        orders = Order.objects.filter(user_id=self.pk, complete=True)

        # sum up all items on the orders
        return sum(o.ambassador_revenue for o in orders)

    objects = UserManager()

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    image = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title} - {self.price}/="

class Link(models.Model):
    code = models.CharField(max_length=255, unique=True) # Order code
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.code} - {self.user.email} ({len(self.products.all())})"

class Order(models.Model):
    transaction_id = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=255)
    ambassador_email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    zip = models.CharField(max_length=255, null=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} by {self.ambassador_email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def ambassador_revenue(self):
        items = OrderItem.objects.filter(order_id=self.pk)
        return sum(i.ambassador_revenue for i in items)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_tile = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    # admin_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    # ambassador_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def admin_revenue(self):
        return .9 * self.quantity * self.price
    
    @property
    def ambassador_revenue(self):
        return .1 * self.quantity * self.price

