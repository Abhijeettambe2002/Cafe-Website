from django.contrib import admin

from django.contrib import admin
from .models import (
    juicesvariety,
    Milkshakesvariety,
    Hot_Chocolatesvariety,
    BeavrageSize,
    BeavragePrice,
    AddBeavrageToCart,
)


class juicesvarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "date_added", "type", "desc", "price")


class MilkshakesvarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "date_added", "type", "desc", "price")


class Hot_ChocolatesvarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "date_added", "type", "desc", "price")


class BeavrageSizeAdmin(admin.ModelAdmin):
    list_display = ("size",)


class BeavragePriceAdmin(admin.ModelAdmin):
    list_display = ("size", "price", "juice", "hot_chocolate", "milkshake")


class AddBeavrageToCartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "juice",
        "hot_chocolate",
        "milkshake",
        "size",
        "quantity",
        "added_on",
    )


admin.site.register(juicesvariety, juicesvarietyAdmin)
admin.site.register(Milkshakesvariety, MilkshakesvarietyAdmin)
admin.site.register(Hot_Chocolatesvariety, Hot_ChocolatesvarietyAdmin)
admin.site.register(BeavrageSize, BeavrageSizeAdmin)
admin.site.register(BeavragePrice, BeavragePriceAdmin)
admin.site.register(AddBeavrageToCart, AddBeavrageToCartAdmin)
