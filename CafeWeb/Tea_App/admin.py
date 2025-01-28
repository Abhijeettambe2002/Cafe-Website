from django.contrib import admin

from django.contrib import admin
from .models import teavariety, TeaSize, TeaPrice, AddTeaToCart


class teavarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "date_added", "type", "desc", "price")


class SizeAdmin(admin.ModelAdmin):
    list_display = ("size",)


class TeaPriceAdmin(admin.ModelAdmin):
    list_display = ("size", "price", "tea")


class AddToCartAdmin(admin.ModelAdmin):
    list_display = ("user", "tea", "size", "quantity", "added_on")


admin.site.register(teavariety, teavarietyAdmin)
admin.site.register(TeaSize, SizeAdmin)
admin.site.register(TeaPrice, TeaPriceAdmin)
admin.site.register(AddTeaToCart, AddToCartAdmin)
