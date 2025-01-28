from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class juicesvariety(models.Model):
    BEVRAGE_TYPE_CHOICES = [
        ("AJ", "Apple Juice"),
        ("OJ", "Orange Juice"),
        ("MJ", "Mango Juice"),
        ("PJ", "Pineapple Juice"),
        ("MFJ", "Mixed Fruit Juice"),
        ("SMJ", "Strawberry Juice"),
        ("WJ", "Watermelon Juice"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=BEVRAGE_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="BeavragePrice")
    sizes = models.ManyToManyField("BeavrageSize", related_name="juicesvariety")

    def __str__(self):
        return self.name


class Hot_Chocolatesvariety(models.Model):
    BEVRAGE_TYPE_CHOICES = [
        ("CHC", "Classic Hot Chocolate"),
        ("WHC", "White Hot Chocolate"),
        ("HHC", "Hazelnut Hot Chocolate"),
        ("NHC", "Nutella Hot Chocolate"),
        ("ALHC", "Almond Hot Chocolate"),
        ("CCHC", "Cookies & Cream Hot Chocolate"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=BEVRAGE_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="BeavragePrice")
    sizes = models.ManyToManyField("BeavrageSize", related_name="Hot_Chocolatesvariety")

    def __str__(self):
        return self.name


class Milkshakesvariety(models.Model):
    BEVRAGE_TYPE_CHOICES = [
        ("CM", "Chocolate Milkshake"),
        ("VM", "Vanilla Milkshake"),
        ("SM", "Strawberry Milkshake"),
        ("BM", "Banana Milkshake"),
        ("OCM", "Oreo Cookies & Cream Milkshake"),
        ("NM", "Nutella Milkshake"),
        ("MM", "Mango Milkshake"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=BEVRAGE_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="BeavragePrice")
    sizes = models.ManyToManyField("BeavrageSize", related_name="Milkshakesvariety")

    def __str__(self):
        return self.name


class BeavrageSize(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

    def __str__(self):
        return self.get_size_display()


class BeavragePrice(models.Model):
    juice = models.ForeignKey(
        juicesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    hot_chocolate = models.ForeignKey(
        Hot_Chocolatesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    milkshake = models.ForeignKey(
        Milkshakesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    size = models.ForeignKey(BeavrageSize, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        beverage_name = ""
        if self.juice:
            beverage_name = self.juice.name
        elif self.hot_chocolate:
            beverage_name = self.hot_chocolate.name
        elif self.milkshake:
            beverage_name = self.milkshake.name
        return f"{beverage_name} ({self.size.get_size_display()}): {self.price} Rs"


class AddBeavrageToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    juice = models.ForeignKey(
        juicesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    hot_chocolate = models.ForeignKey(
        Hot_Chocolatesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    milkshake = models.ForeignKey(
        Milkshakesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    size = models.ForeignKey(BeavrageSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        beverage_name = ""
        if self.juice:
            beverage_name = self.juice.name
        elif self.hot_chocolate:
            beverage_name = self.hot_chocolate.name
        elif self.milkshake:
            beverage_name = self.milkshake.name
        return f"{self.user.username} - {beverage_name} ({self.size.get_size_display()}) x {self.quantity}"
