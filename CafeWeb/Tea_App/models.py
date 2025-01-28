from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class teavariety(models.Model):
    TEA_TYPE_CHOICES = [
        ("GB", "Green Tea"),
        ("BL", "Black Tea"),
        ("WH", "White Tea"),
        ("OL", "Oolong Tea"),
        ("MR", "Matcha"),
        ("CH", "Chai"),
        ("DA", "Darjeeling"),
        ("HB", "Herbal Tea"),
        ("LF", "Lemon Verbena"),
        ("AS", "Assam Tea"),
        ("NI", "Nilgiri Tea"),
        ("KJ", "Kashmiri Kahwa"),
        ("CL", "Chrysanthemum Tea"),
        ("MA", "Masala Chai"),
        ("TT", "Tandoori Chai"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cafe/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=TEA_TYPE_CHOICES)
    desc = models.TextField(default="")
    price = models.IntegerField(default=0, verbose_name="TeaPrice")
    sizes = models.ManyToManyField("TeaSize", related_name="teavariety")

    def __str__(self):
        return self.name


class TeaSize(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

    def __str__(self):
        return self.get_size_display()


class TeaPrice(models.Model):
    tea = models.ForeignKey(teavariety, on_delete=models.CASCADE)
    size = models.ForeignKey(TeaSize, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.tea.name} ({self.size.get_size_display()}): {self.price} Rs"


class AddTeaToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tea = models.ForeignKey(teavariety, on_delete=models.CASCADE)
    size = models.ForeignKey(TeaSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tea.name} ({self.size.get_size_display()}) x {self.quantity}"


# Create your models here.
