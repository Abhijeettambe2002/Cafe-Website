from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class coffeevariety(models.Model):
    COFFEE_TYPE_CHOICES = [
        ("EX", "Espresso"),
        ("AM", "Americano"),
        ("LT", "Latte"),
        ("CP", "Cappuccino"),
        ("MC", "Macchiato"),
        ("MO", "Mocha"),
        ("FW", "Flat White"),
        ("RS", "Ristretto"),
        ("CB", "Cold Brew"),
        ("FP", "French Press"),
        ("TK", "Turkish Coffee"),
        ("AF", "Affogato"),
        ("FR", "Frappuccino"),
        ("BR", "Caffè Breve"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=COFFEE_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="Coffee Price")
    sizes = models.ManyToManyField("Size", related_name="coffee_varieties")

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

    def __str__(self):
        return self.get_size_display()


class CoffeePrice(models.Model):
    coffee = models.ForeignKey(coffeevariety, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.coffee.name} ({self.size.get_size_display()}): {self.price} Rs"


class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee = models.ForeignKey(coffeevariety, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.coffee.name} ({self.size.get_size_display()}) x {self.quantity}"


class Store(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CoffeeCertificate(models.Model):
    coffee = models.OneToOneField(
        coffeevariety, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()


def __str__(self):
    return f"Certificate for {self.coffee.name}"


class Payment(models.Model):
    Card_Num = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    upi = models.CharField(
        max_length=50, blank=True, null=True
    )  # Correctly defined UPI field

    def __str__(self):
        return f"Card ending in {self.Card_Num[-4:] if self.Card_Num else 'N/A'}"


from django.db import models
from django.core.exceptions import ValidationError


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(max_length=10, blank=True, null=True)
    message = models.TextField(default=None)

    def clean(self):
        if not self.phone_number and not self.email:
            raise ValidationError("Either phone number or email must be provided.")

    def __str__(self):

        return f"Message from {self.phone_number or self.email}"
