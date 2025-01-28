from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Snacksvariety(models.Model):
    FOOD_TYPE_CHOICES = [
        ("CB", "Chicken Burger"),
        ("BG", "BBQ Chicken Wrap"),
        ("GR", "Grilled Cheese Sandwich"),
        ("VB", "Veggie Burger"),
        ("PB", "Paneer Tikka Wrap"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=FOOD_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="FoodPrice")
    sizes = models.ManyToManyField("FoodSize", related_name="Snacksvariety")

    def __str__(self):
        return self.name


class Side_dishvariety(models.Model):
    FOOD_TYPE_CHOICES = [
        ("FN", "French Fries"),
        ("GC", "Garlic Bread"),
        ("NM", "Nachos with Cheese"),
        ("SM", "Samosas"),
        ("CB", "Cheese Balls"),
        ("CP", "Classic Pizza"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=FOOD_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="FoodPrice")
    sizes = models.ManyToManyField("FoodSize", related_name="Side_dishvariety")

    def __str__(self):
        return self.name


class Pastasvariety(models.Model):
    FOOD_TYPE_CHOICES = [
        ("SP", "Spaghetti Bolognese"),
        ("CP", "Creamy Fettuccine Alfredo"),
        ("MP", "Macaroni & Cheese"),
        ("PP", "Pesto Pasta"),
        ("CM", "Classic Masala Maggi"),
        ("BM", "Butter Garlic Maggi"),
        ("ChM", "Cheese Maggi"),
        ("VDM", "Veggie Delight Maggi"),
        ("SSM", "Spicy Schezwan Maggi"),
        ("PM", "Paneer Maggi"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=FOOD_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="FoodPrice")
    sizes = models.ManyToManyField("FoodSize", related_name="Pastasvariety")

    def __str__(self):
        return self.name


class FoodSize(models.Model):
    SIZE_CHOICES = [
        ("R", "Regular"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)

    def __str__(self):
        return self.get_size_display()


class FoodPrice(models.Model):
    Snacks = models.ForeignKey(
        Snacksvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Side_dish = models.ForeignKey(
        Side_dishvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Pastas = models.ForeignKey(
        Pastasvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    size = models.ForeignKey(FoodSize, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        food_name = ""
        if self.Snacks:
            food_name = self.Snacks.name
        elif self.Side_dish:
            food_name = self.Side_dish.name
        elif self.Pastas:
            food_name = self.Pastas.name
        return f"{food_name} ({self.size.get_size_display()}): {self.price} Rs"


class AddFoodToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Snacks = models.ForeignKey(
        Snacksvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Side_dish = models.ForeignKey(
        Side_dishvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Pastas = models.ForeignKey(
        Pastasvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    size = models.ForeignKey(FoodSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        food_name = ""
        if self.Snacks:
            food_name = self.Snacks.name
        elif self.Side_dish:
            food_name = self.Side_dish.name
        elif self.Pastas:
            food_name = self.Pastas.name
        return f"{self.user.username} - {food_name} ({self.size.get_size_display()}) x {self.quantity}"
