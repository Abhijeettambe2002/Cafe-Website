from django.shortcuts import render, redirect
from CafeApp.models import (
    coffeevariety,
    Size,
    CoffeePrice,
    Payment,
    AddToCart,
    Contact,
    Store,
)
from SoldApp.models import SoldItem
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import logout
from .forms import coffeevarietyForm, PaymentForm, RegistrationForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from Tea_App.models import teavariety, TeaPrice, AddTeaToCart, TeaSize
from Other_Beverage.models import (
    juicesvariety,
    Milkshakesvariety,
    Hot_Chocolatesvariety,
    BeavrageSize,
    BeavragePrice,
    AddBeavrageToCart,
)
from Food_App.models import (
    AddFoodToCart,
    Snacksvariety,
    Side_dishvariety,
    Pastasvariety,
    FoodSize,
    FoodPrice,
)
from DeliveryInfo.models import DeliveryInformation
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import DeliveryInformationForm




def user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect("main_page")
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_page")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("login_page")


def main_page(request):
    coffees = coffeevariety.objects.order_by("?")[:4]
    sizes = Size.objects.all()
    coffee_prices = CoffeePrice.objects.all()
    teas = teavariety.objects.order_by("?")[:4]
    tea_sizes = TeaSize.objects.all()
    tea_prices = TeaPrice.objects.all()
    juices = juicesvariety.objects.order_by("?")[:2]
    hot_chocolates = Hot_Chocolatesvariety.objects.order_by("?").first()
    milkshakes = Milkshakesvariety.objects.order_by("?").first()
    beverage_sizes = BeavrageSize.objects.all()
    beverage_prices = BeavragePrice.objects.all()
    snacks = Snacksvariety.objects.order_by("?")[:2]
    side_dishes = Side_dishvariety.objects.order_by("?").first()
    pastas = Pastasvariety.objects.order_by("?").first()
    food_sizes = FoodSize.objects.all()
    food_prices = FoodPrice.objects.all()
    return render(
        request,
        "mainpage.html",
        {
            "coffees": coffees,
            "sizes": sizes,
            "coffee_prices": coffee_prices,
            "teas": teas,
            "tea_sizes": tea_sizes,
            "tea_prices": tea_prices,
            "juices": juices,
            "hot_chocolates": hot_chocolates,
            "milkshakes": milkshakes,
            "beverage_sizes": beverage_sizes,
            "beverage_prices": beverage_prices,
            "snacks": snacks,
            "side_dishes": side_dishes,
            "pastas": pastas,
            "food_sizes": food_sizes,
            "food_prices": food_prices,
        },
    )


def all_coffees(request):
    coffees = coffeevariety.objects.all()
    sizes = Size.objects.all()
    coffee_prices = CoffeePrice.objects.all()
    return render(
        request,
        "all_coffees.html",
        {
            "coffees": coffees,
            "sizes": sizes,
            "coffee_prices": coffee_prices,
        },
    )


def all_Tea(request):
    teas = teavariety.objects.all()
    tea_sizes = TeaSize.objects.all()
    tea_prices = TeaPrice.objects.all()
    return render(
        request,
        "all_Tea.html",
        {
            "teas": teas,
            "tea_sizes": tea_sizes,
            "tea_prices": tea_prices,
        },
    )


def other_beverages(request):
    juices = juicesvariety.objects.all()
    hot_chocolates = Hot_Chocolatesvariety.objects.all()
    milkshakes = Milkshakesvariety.objects.all()
    beverage_sizes = BeavrageSize.objects.all()
    beverage_prices = BeavragePrice.objects.all()
    return render(
        request,
        "other_beverages.html",
        {
            "juices": juices,
            "hot_chocolates": hot_chocolates,
            "milkshakes": milkshakes,
            "beverage_sizes": beverage_sizes,
            "beverage_prices": beverage_prices,
        },
    )


def all_food(request):
    snacks = Snacksvariety.objects.all()
    side_dishes = Side_dishvariety.objects.all()
    pastas = Pastasvariety.objects.all()
    food_sizes = FoodSize.objects.all()
    food_prices = FoodPrice.objects.all()
    return render(
        request,
        "all_food.html",
        {
            "snacks": snacks,
            "side_dishes": side_dishes,
            "pastas": pastas,
            "food_sizes": food_sizes,
            "food_prices": food_prices,
        },
    )


def coffee_details(request, cafe_id):
    coffee = get_object_or_404(coffeevariety, pk=cafe_id)
    return render(request, "coffee_details.html", {"coffee": coffee})


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data["message"]

            emp = Contact.objects.create(
                name=name, email=email, phone_number=phone_number, message=message
            )

            emp.save()
            return HttpResponseRedirect("the data is saved")
    form = ContactForm()
    return render(request, "contact.html", {"form": form})


from django.shortcuts import render, redirect
from .forms import DeliveryInformationForm


from django.shortcuts import render, redirect
from .forms import DeliveryInformationForm
from DeliveryInfo.models import DeliveryInformation


def delivery_information_view(request):
    delivery_info = DeliveryInformation.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = DeliveryInformationForm(request.POST, instance=delivery_info)
        if form.is_valid():
            delivery_info = form.save(commit=False)
            delivery_info.user = request.user
            delivery_info.save()
            return redirect("main_page")  
    else:
        form = DeliveryInformationForm(instance=delivery_info)

    return render(
        request,
        "delivery_information.html",
        {"form": form, "delivery_info": delivery_info},
    )


def cart_view(request):
    delivery_info = DeliveryInformation.objects.filter(user=request.user).first()

    coffee_items = AddToCart.objects.filter(user=request.user).select_related(
        "coffee", "size"
    )

    tea_items = AddTeaToCart.objects.filter(user=request.user).select_related(
        "tea", "size"
    )
    juice_items = AddBeavrageToCart.objects.filter(
        user=request.user, juice__isnull=False
    ).select_related("juice", "size")

    hot_chocolate_items = AddBeavrageToCart.objects.filter(
        user=request.user, hot_chocolate__isnull=False
    ).select_related("hot_chocolate", "size")

    milkshake_items = AddBeavrageToCart.objects.filter(
        user=request.user, milkshake__isnull=False
    ).select_related("milkshake", "size")

    snack_items = AddFoodToCart.objects.filter(
        user=request.user, Snacks__isnull=False
    ).select_related("Snacks", "size")
    side_dish_items = AddFoodToCart.objects.filter(
        user=request.user, Side_dish__isnull=False
    ).select_related("Side_dish", "size")
    pasta_items = AddFoodToCart.objects.filter(
        user=request.user, Pastas__isnull=False
    ).select_related("Pastas", "size")

    cart_items_with_prices = []
    total_price = 0
    for item in coffee_items:
        try:
            price = CoffeePrice.objects.get(coffee=item.coffee, size=item.size).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "coffee",
                }
            )
        except CoffeePrice.DoesNotExist:
            continue
    for item in tea_items:
        try:
            price = TeaPrice.objects.get(tea=item.tea, size=item.size).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "tea",
                }
            )
        except TeaPrice.DoesNotExist:
            continue

    for item in juice_items:
        try:
            price = BeavragePrice.objects.get(juice=item.juice, size=item.size).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "juice",
                }
            )
        except BeavragePrice.DoesNotExist:
            continue
    for item in hot_chocolate_items:
        try:
            price = BeavragePrice.objects.get(
                hot_chocolate=item.hot_chocolate, size=item.size
            ).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "hot_chocolate",
                }
            )
        except BeavragePrice.DoesNotExist:
            continue
    for item in milkshake_items:
        try:
            price = BeavragePrice.objects.get(
                milkshake=item.milkshake, size=item.size
            ).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "milkshake",
                }
            )
        except BeavragePrice.DoesNotExist:
            continue
    for item in snack_items:
        try:
            price = FoodPrice.objects.get(Snacks=item.Snacks, size=item.size).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "snack",
                }
            )
        except FoodPrice.DoesNotExist:
            continue
    for item in side_dish_items:
        try:
            price = FoodPrice.objects.get(
                Side_dish=item.Side_dish, size=item.size
            ).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "side_dish",
                }
            )
        except FoodPrice.DoesNotExist:
            continue

    for item in pasta_items:
        try:
            price = FoodPrice.objects.get(Pastas=item.Pastas, size=item.size).price
            total_price += price * item.quantity
            cart_items_with_prices.append(
                {
                    "item": item,
                    "price": price,
                    "subtotal": price * item.quantity,
                    "type": "pasta",
                }
            )
        except FoodPrice.DoesNotExist:
            continue

    return render(
        request,
        "cart.html",
        {
            "cart_items_with_prices": cart_items_with_prices,
            "total_price": total_price,
            "delivery_info": delivery_info,
        },
    )


def update_address_view(request):
    delivery_info = get_object_or_404(DeliveryInformation, user=request.user)
    if request.method == "POST":
        form = DeliveryInformationForm(request.POST, instance=delivery_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Address updated successfully.")
            return redirect("main_page")
    else:
        form = DeliveryInformationForm(instance=delivery_info)
    return render(request, "update_address.html", {"form": form})


def delete_address_view(request):
    delivery_info = get_object_or_404(DeliveryInformation, user=request.user)
    if request.method == "POST":
        delivery_info.delete()
        messages.success(request, "Address deleted successfully.")
        return redirect("main_page")

    return render(request, "delete_address.html", {"delivery_info": delivery_info})


def add_to_cart(request, coffee_id, size_id, action):
    coffee = coffeevariety.objects.get(id=coffee_id)
    size = Size.objects.get(id=size_id)
    cart_item, created = AddToCart.objects.get_or_create(
        user=request.user, coffee=coffee, size=size, defaults={"quantity": 1}
    )
    if not created:
        if action == "increment":
            cart_item.quantity += 1
        elif action == "decrement":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
                return redirect("cart_view")
        cart_item.save()
    return redirect("cart_view")


def add_tea_to_cart(request, tea_id, size_id, action):
    tea = teavariety.objects.get(id=tea_id)
    size = TeaSize.objects.get(id=size_id)
    cart_item, created = AddTeaToCart.objects.get_or_create(
        user=request.user, tea=tea, size=size, defaults={"quantity": 1}
    )
    if not created:
        if action == "increment":
            cart_item.quantity += 1
        elif action == "decrement":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
                return redirect("cart_view")
        cart_item.save()
    return redirect("cart_view")


def add_beverage_to_cart(request, beverage_type, beverage_id, size_id, action):
    beverage = None
    if beverage_type == "juice":
        beverage = get_object_or_404(juicesvariety, id=beverage_id)
    elif beverage_type == "hot_chocolate":
        beverage = get_object_or_404(Hot_Chocolatesvariety, id=beverage_id)
    elif beverage_type == "milkshake":
        beverage = get_object_or_404(Milkshakesvariety, id=beverage_id)

    size = get_object_or_404(BeavrageSize, id=size_id)
    cart_item, created = AddBeavrageToCart.objects.get_or_create(
        user=request.user,
        juice=beverage if isinstance(beverage, juicesvariety) else None,
        hot_chocolate=beverage if isinstance(beverage, Hot_Chocolatesvariety) else None,
        milkshake=beverage if isinstance(beverage, Milkshakesvariety) else None,
        size=size,
        defaults={"quantity": 1},
    )
    if not created:
        if action == "increment":
            cart_item.quantity += 1
        elif action == "decrement":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
                return redirect("cart_view")
        cart_item.save()
    return redirect("cart_view")


def add_food_to_cart(request, food_type, food_id, size_id, action):
    food = None
    if food_type == "snack":
        food = get_object_or_404(Snacksvariety, id=food_id)
    elif food_type == "side_dish":
        food = get_object_or_404(Side_dishvariety, id=food_id)
    elif food_type == "pasta":
        food = get_object_or_404(Pastasvariety, id=food_id)

    size = get_object_or_404(FoodSize, id=size_id)
    cart_item, created = AddFoodToCart.objects.get_or_create(
        user=request.user,
        Snacks=food if isinstance(food, Snacksvariety) else None,
        Side_dish=food if isinstance(food, Side_dishvariety) else None,
        Pastas=food if isinstance(food, Pastasvariety) else None,
        size=size,
        defaults={"quantity": 1},
    )
    if not created:
        if action == "increment":
            cart_item.quantity += 1
        elif action == "decrement":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
                return redirect("cart_view")
        cart_item.save()
    return redirect("cart_view")


def delete_from_cart(request, item_id, item_type):
    if item_type == "coffee":
        cart_item = get_object_or_404(AddToCart, id=item_id, user=request.user)
    elif item_type == "tea":
        cart_item = get_object_or_404(AddTeaToCart, id=item_id, user=request.user)
    elif item_type == "juice":
        cart_item = get_object_or_404(
            AddBeavrageToCart, id=item_id, user=request.user, juice__isnull=False
        )
    elif item_type == "hot_chocolate":
        cart_item = get_object_or_404(
            AddBeavrageToCart,
            id=item_id,
            user=request.user,
            hot_chocolate__isnull=False,
        )
    elif item_type == "milkshake":
        cart_item = get_object_or_404(
            AddBeavrageToCart, id=item_id, user=request.user, milkshake__isnull=False
        )
    elif item_type == "snack":
        cart_item = get_object_or_404(
            AddFoodToCart, id=item_id, user=request.user, Snacks__isnull=False
        )
    elif item_type == "side_dish":
        cart_item = get_object_or_404(
            AddFoodToCart, id=item_id, user=request.user, Side_dish__isnull=False
        )
    elif item_type == "pasta":
        cart_item = get_object_or_404(
            AddFoodToCart, id=item_id, user=request.user, Pastas__isnull=False
        )
    else:
        return redirect("cart_view")

    cart_item.delete()
    return redirect("cart_view")


def coffee_store_view(request):
    stores = None
    coffee_type_exists = True
    selected_coffee = None
    city = None
    if request.method == "POST":
        form = coffeevarietyForm(request.POST)
        if form.is_valid():
            coffee_types = form.cleaned_data.get("coffee_types")
            selected_coffee = coffee_types.name if coffee_types else "selected type"
            city = form.cleaned_data.get("city")
            if coffee_types and city:
                stores = Store.objects.filter(coffee_varieties=coffee_types, city=city)
                if not stores.exists():
                    stores = Store.objects.filter(city=city)
                    coffee_type_exists = False
            elif coffee_types:
                stores = Store.objects.filter(coffee_varieties=coffee_types)
            elif city:
                stores = Store.objects.filter(city=city)
    else:
        form = coffeevarietyForm()

    return render(
        request,
        "Stores.html",
        {
            "form": form,
            "stores": stores,
            "coffee_type_exists": coffee_type_exists,
            "selected_coffee": selected_coffee,
            "city": city,
        },
    )


def payment_success(request):
    return render(request, "success.html")


def logout_view(request):
    logout(request)
    return redirect("all_coffees")




def payment_view(request):
    if not DeliveryInformation.objects.filter(user=request.user).exists():
        return redirect("delivery_information_view")
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data["choice"]

            if choice == "upi":
                upi = form.cleaned_data["upi"]
                if not upi:
                    form.add_error("upi", "UPI ID is required for UPI payment.")
                else:
                    payment = Payment.objects.create(upi=upi)
                    payment.save()

            elif choice == "card":
                Card_Num = form.cleaned_data["Card_Num"]
                expiry_date = form.cleaned_data["expiry_date"]
                if not Card_Num:
                    form.add_error(
                        "Card_Num", "Card number is required for card payment."
                    )
                if not expiry_date:
                    form.add_error(
                        "expiry_date", "Expiry date is required for card payment."
                    )
                if Card_Num and expiry_date:
                    payment = Payment.objects.create(
                        Card_Num=Card_Num, expiry_date=expiry_date
                    )
                    payment.save()

            if not form.errors:
                coffee_cart_items = AddToCart.objects.filter(user=request.user)
                tea_cart_items = AddTeaToCart.objects.filter(user=request.user)
                juice_cart_items = AddBeavrageToCart.objects.filter(
                    user=request.user, juice__isnull=False
                )
                hot_chocolate_cart_items = AddBeavrageToCart.objects.filter(
                    user=request.user, hot_chocolate__isnull=False
                )
                milkshake_cart_items = AddBeavrageToCart.objects.filter(
                    user=request.user, milkshake__isnull=False
                )
                snack_cart_items = AddFoodToCart.objects.filter(
                    user=request.user, Snacks__isnull=False
                )
                side_dish_cart_items = AddFoodToCart.objects.filter(
                    user=request.user, Side_dish__isnull=False
                )
                pasta_cart_items = AddFoodToCart.objects.filter(
                    user=request.user, Pastas__isnull=False
                )

                for item in coffee_cart_items:
                    if item.coffee:
                        price = CoffeePrice.objects.get(
                            coffee=item.coffee, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            coffee=item.coffee,
                            size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in tea_cart_items:
                    if item.tea:
                        price = TeaPrice.objects.get(tea=item.tea, size=item.size).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            tea=item.tea,
                            tea_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in juice_cart_items:
                    if item.juice:
                        price = BeavragePrice.objects.get(
                            juice=item.juice, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            juice=item.juice,
                            beverage_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in hot_chocolate_cart_items:
                    if item.hot_chocolate:
                        price = BeavragePrice.objects.get(
                            hot_chocolate=item.hot_chocolate, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            hot_chocolate=item.hot_chocolate,
                            beverage_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in milkshake_cart_items:
                    if item.milkshake:
                        price = BeavragePrice.objects.get(
                            milkshake=item.milkshake, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            milkshake=item.milkshake,
                            beverage_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in snack_cart_items:
                    if item.Snacks:
                        price = FoodPrice.objects.get(
                            Snacks=item.Snacks, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            Snacks=item.Snacks,
                            food_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in side_dish_cart_items:
                    if item.Side_dish:
                        price = FoodPrice.objects.get(
                            Side_dish=item.Side_dish, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            Side_dish=item.Side_dish,
                            food_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                for item in pasta_cart_items:
                    if item.Pastas:
                        price = FoodPrice.objects.get(
                            Pastas=item.Pastas, size=item.size
                        ).price
                        amount_paid = price * item.quantity
                        SoldItem.objects.create(
                            user=item.user,
                            Pastas=item.Pastas,
                            food_size=item.size,
                            quantity=item.quantity,
                            price=price,
                            amount_paid=amount_paid,
                            payment_method=choice,
                            card_num=payment.Card_Num if choice == "card" else None,
                            expiry_date=(
                                payment.expiry_date if choice == "card" else None
                            ),
                            upi=payment.upi if choice == "upi" else None,
                            sold_on=timezone.now(),
                        )

                coffee_cart_items.delete()
                tea_cart_items.delete()
                juice_cart_items.delete()
                hot_chocolate_cart_items.delete()
                milkshake_cart_items.delete()
                snack_cart_items.delete()
                side_dish_cart_items.delete()
                pasta_cart_items.delete()
                messages.success(
                    request, "Payment successful. Your cart has been cleared."
                )
                return HttpResponseRedirect("/payment/success")
    else:
        form = PaymentForm()

    return render(request, "pay.html", {"form": form})
