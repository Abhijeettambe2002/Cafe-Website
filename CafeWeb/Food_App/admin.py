from django.contrib import admin
from .models import (
    Snacksvariety,
    Side_dishvariety,
    Pastasvariety,
    FoodSize,
    FoodPrice,
    AddFoodToCart,
)


# Register your models here.
class SnacksvarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image", "date_added", "type", "desc")


class Side_dishvarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image", "date_added", "type", "desc")


class PastasvarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image", "date_added", "type", "desc")


class FoodSizeAdmin(admin.ModelAdmin):
    list_display = ("size",)


class FoodPriceAdmin(admin.ModelAdmin):
    list_display = ("size", "price", "Snacks", "Side_dish", "Pastas")


class AddFoodToCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "Snacks",
        "Side_dish",
        "Pastas",
        "size",
        "quantity",
        "added_on",
    )


admin.site.register(Snacksvariety, SnacksvarietyAdmin)
admin.site.register(Side_dishvariety, Side_dishvarietyAdmin)
admin.site.register(Pastasvariety, PastasvarietyAdmin)
admin.site.register(FoodSize, FoodSizeAdmin)
admin.site.register(FoodPrice, FoodPriceAdmin)
admin.site.register(AddFoodToCart, AddFoodToCartAdmin)
