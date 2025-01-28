from django.contrib import admin

from .models import DeliveryInformation


class DeliveryInformationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "name",
        "email",
        "phone_number",
        "landmark",
        "address",
        "city",
        "zip_code",
    ]


admin.site.register(DeliveryInformation, DeliveryInformationAdmin)

# Register your models here.
