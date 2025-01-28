from django.db import models
from CafeApp.models import coffeevariety, Size
from Tea_App.models import teavariety, TeaSize
from Other_Beverage.models import (
    juicesvariety,
    Milkshakesvariety,
    Hot_Chocolatesvariety,
    BeavrageSize,
)
from Food_App.models import Snacksvariety, Side_dishvariety, Pastasvariety, FoodSize
from django.contrib.auth.models import User


class SoldItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee = models.ForeignKey(
        coffeevariety, null=True, blank=True, on_delete=models.CASCADE
    )
    tea = models.ForeignKey(teavariety, null=True, blank=True, on_delete=models.CASCADE)
    juice = models.ForeignKey(
        juicesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    hot_chocolate = models.ForeignKey(
        Hot_Chocolatesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    milkshake = models.ForeignKey(
        Milkshakesvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Snacks = models.ForeignKey(
        Snacksvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Side_dish = models.ForeignKey(
        Side_dishvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    Pastas = models.ForeignKey(
        Pastasvariety, null=True, blank=True, on_delete=models.CASCADE
    )
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.CASCADE)
    tea_size = models.ForeignKey(
        TeaSize, null=True, blank=True, on_delete=models.CASCADE
    )
    beverage_size = models.ForeignKey(
        BeavrageSize, null=True, blank=True, on_delete=models.CASCADE
    )
    food_size = models.ForeignKey(
        FoodSize, null=True, blank=True, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    card_num = models.CharField(max_length=20, null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    upi = models.CharField(max_length=50, null=True, blank=True)
    sold_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.coffee:
            return f"{self.user.username} bought {self.quantity} x {self.coffee.name} ({self.size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.tea:
            return f"{self.user.username} bought {self.quantity} x {self.tea.name} ({self.tea_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.juice:
            return f"{self.user.username} bought {self.quantity} x {self.juice.name} ({self.beverage_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.hot_chocolate:
            return f"{self.user.username} bought {self.quantity} x {self.hot_chocolate.name} ({self.beverage_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.milkshake:
            return f"{self.user.username} bought {self.quantity} x {self.milkshake.name} ({self.beverage_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.Snacks:
            return f"{self.user.username} bought {self.quantity} x {self.Snacks.name} ({self.food_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.Side_dish:
            return f"{self.user.username} bought {self.quantity} x {self.Side_dish.name} ({self.food_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        elif self.Pastas:
            return f"{self.user.username} bought {self.quantity} x {self.Pastas.name} ({self.food_size.get_size_display()}) for {self.amount_paid} Rs on {self.sold_on}"
        else:
            return f"{self.user.username} bought {self.quantity} items for {self.amount_paid} Rs on {self.sold_on}"
