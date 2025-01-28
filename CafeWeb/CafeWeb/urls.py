"""
URL configuration for CafeWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.user, name="user"),
    path("logout_page/", views.logout_page, name="logout_page"),
    path("login_page/", views.login_page, name="login_page"),
    path("main_page/", views.main_page, name="main_page"),
    path("all_coffees/", views.all_coffees, name="all_coffees"),
    path("all_Tea/", views.all_Tea, name="all_Tea"),
    path("other_beverages/", views.other_beverages, name="other_beverages"),
    path("all_food/", views.all_food, name="all_food"),
    path(
        "delivery_information_view/",
        views.delivery_information_view,
        name="delivery_information_view",
    ),
    path("update_address_view/", views.update_address_view, name="update_address_view"),
    path("delete_address_view/", views.delete_address_view, name="delete_address_view"),
    path("<int:cafe_id>/", views.coffee_details, name="coffee_details"),
    path("cart_view/", views.cart_view, name="cart_view"),
    path(
        "add-to-cart/<int:coffee_id>/<int:size_id>/<str:action>/",
        views.add_to_cart,
        name="add_to_cart",
    ),
    path(
        "add_tea_to_cart/<int:tea_id>/<int:size_id>/<str:action>/",
        views.add_tea_to_cart,
        name="add_tea_to_cart",
    ),
    path(
        "add_beverage_to_cart/<str:beverage_type>/<int:beverage_id>/<int:size_id>/<str:action>/",
        views.add_beverage_to_cart,
        name="add_beverage_to_cart",
    ),
    path(
        "add_food_to_cart/<str:food_type>/<int:food_id>/<int:size_id>/<str:action>/",
        views.add_food_to_cart,
        name="add_food_to_cart",
    ),
    path(
        "delete_from_cart/<int:item_id>/<str:item_type>/",
        views.delete_from_cart,
        name="delete_from_cart",
    ),
    path("coffee_store_view/", views.coffee_store_view, name="coffee_store_view"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("payment/", views.payment_view, name="payment_view"),
    path("logout/", views.logout_view, name="logout"),
    path("contact_us/", views.contact_us, name="contact_us"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
