from django.contrib import admin
from django.contrib import admin
from .models import (
    coffeevariety,
    Size,
    CoffeePrice,
    AddToCart,
    Store,
    CoffeeCertificate,
    Payment,
    Contact,
)


class coffeevarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "date_added", "type", "desc", "price")


class SizeAdmin(admin.ModelAdmin):
    list_display = ("size",)


class CoffeePriceAdmin(admin.ModelAdmin):
    list_display = ("size", "price", "coffee")


class AddToCartAdmin(admin.ModelAdmin):
    list_display = ("size", "coffee", "user", "quantity", "added_on")


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


class CoffeeCertificateAdmin(admin.ModelAdmin):
    list_display = ("coffee", "certificate_number", "issued_date", "valid_until")


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("Card_Num", "expiry_date")


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "message")


admin.site.register(coffeevariety, coffeevarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(CoffeeCertificate, CoffeeCertificateAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(CoffeePrice, CoffeePriceAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(AddToCart, AddToCartAdmin)
admin.site.register(Contact, ContactAdmin)


# Register your models here.


# Register your models here.
