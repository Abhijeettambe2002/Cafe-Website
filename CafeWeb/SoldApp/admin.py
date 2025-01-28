from django.contrib import admin

from .models import SoldItem


class SoldItemAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "coffee",
        "tea",
        "tea_size",
        "size",
        "juice",
        "hot_chocolate",
        "milkshake",
        "Snacks",
        "Side_dish",
        "Pastas",
        "food_size",
        "beverage_size",
        "quantity",
        "price",
        "amount_paid",
        "payment_method",
        "card_num",
        "expiry_date",
        "upi",
        "sold_on",
    )


admin.site.register(SoldItem, SoldItemAdmin)
# Register your models here.
