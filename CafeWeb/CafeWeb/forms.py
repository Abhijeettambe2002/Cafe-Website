from django import forms
from CafeApp.models import Contact, coffeevariety, Size, Payment
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from DeliveryInfo.models import DeliveryInformation


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{10,}$",
                message="Please enter a valid phone number with at least 10 digits.",
                code="invalid_phone_number",
            )
        ],
    )
    message = forms.CharField(widget=forms.Textarea)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit():
            raise ValidationError("Please enter a valid phone number with only digits.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone_number = cleaned_data.get("phone_number")

        if not email and not phone_number:
            raise forms.ValidationError(
                "Either phone number or email must be provided."
            )


class coffeevarietyForm(forms.Form):
    city = forms.CharField(max_length=100, label="City", required=True)

    def clean_city(self):
        city = self.cleaned_data.get("city")
        if city:
            city = city.strip().title()
        return city


from django import forms


def validate_upi(value):
    if "@" not in value:
        raise ValidationError("UPI ID must contain '@'.")


class PaymentForm(forms.ModelForm):
    CHOICES = [
        ("upi", "UPI"),
        ("card", "Card Payment"),
    ]

    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    upi = forms.CharField(max_length=50, required=False, help_text="Enter your UPI ID")
    Card_Num = forms.CharField(max_length=16, required=False)
    expiry_date = forms.DateField(
        input_formats=["%Y-%m"],  
        widget=forms.DateInput(attrs={"type": "month"}),
        required=False,
    )

    class Meta:
        model = Payment
        fields = ["choice", "upi", "Card_Num", "expiry_date"]


class DeliveryInformationForm(forms.ModelForm):
    class Meta:
        model = DeliveryInformation
        fields = [
            "name",
            "email",
            "phone_number",
            "landmark",
            "address",
            "city",
            "zip_code",
        ]
