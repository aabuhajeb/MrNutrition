from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(max_length=8, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="no bio...", max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Product(models.Model):
    TYPE = (
        ('Bars' , 'Bars'),
        ('Drinks' , 'Drinks'),
        ('Powder' , 'Powder'),
        ('Tablets & Capsules' , 'Tablets & Capsules')
    )
    FLAVOR = (
        ('Chocolate' , 'Chocolate'),
        ('Snickerdoodle' , 'Snickerdoodle'),
        ('Cookies & Cream' , 'Cookies & Cream'),
        ('Strawberry' , 'Strawberry'),
        ('Vanilla' , 'Vanilla'),
        ('Fruits' , 'Fruits'),
    )
    MANUFACTURE = (
        ('Kabs' , 'Kabs'),
        ('First Nutrition' , 'First Nutrition'),
        ('Go Tamreen' , 'Go Tamreen'),
        ('Supplements Mall' , 'Supplements Mall'),
        ('Protinak' , 'Protinak'),
    )

    FOODTYPE = (
        ('Salad' , 'Salad'),
        ('Drinks' , 'Drinks'),
        ('Protin' , 'Protin'),
        ('Carbs' , 'Carbs'),
    )
    FOODSIZE = (
        ('20g' , '20g'),
        ('50g' , '50g'),
        ('80g' , '80g'),
        ('100g' , '100g'),
        ('150g' , '150g'),
        ('200g' , '200g'),
    )
    FOODMANUFACTURE = (
        ('Muscle Kitchen' , 'Muscle Kitchen'),
        ('Thefitbar' , 'Thefitbar'),
        ('Fit Food Factory' , 'Fit Food Factory'),
        ('Calories Healthy Food Resturant' , 'Calories Healthy Food Resturant'),
        ("OJ's - Super Fast Salads" , "OJ's - Super Fast Salads"),
    )

    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ptype = models.CharField(max_length=200, null=True, choices=TYPE)
    flavor = models.CharField(max_length=200, null=True, choices=FLAVOR)
    manufacture = models.CharField(max_length=200, null=True, choices=MANUFACTURE)
    food_type = models.CharField(max_length=200, null=True, choices=FOODTYPE)
    food_flavor = models.CharField(max_length=200, null=True, choices=FOODSIZE)
    food_manufacture = models.CharField(max_length=200, null=True, choices=FOODMANUFACTURE)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0 )
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    rating =   models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.rating)

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

         
class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    address = models.CharField(null=True, max_length=200)
    city = models.CharField(null=False, max_length=200)
    zipcode = models.CharField(null=False, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address