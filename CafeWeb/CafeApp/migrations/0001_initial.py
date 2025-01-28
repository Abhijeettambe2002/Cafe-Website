# Generated by Django 5.1.5 on 2025-01-21 12:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='coffeevariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cafe/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('EX', 'Espresso'), ('AM', 'Americano'), ('LT', 'Latte'), ('CP', 'Cappuccino'), ('MC', 'Macchiato'), ('MO', 'Mocha'), ('FW', 'Flat White'), ('RS', 'Ristretto'), ('CB', 'Cold Brew'), ('FP', 'French Press'), ('TK', 'Turkish Coffee'), ('AF', 'Affogato'), ('FR', 'Frappuccino'), ('BR', 'Caffè Breve')], max_length=3)),
                ('desc', models.TextField(default='')),
                ('price', models.IntegerField(default=0, verbose_name='Coffee Price')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.IntegerField(blank=True, max_length=10, null=True)),
                ('message', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Card_Num', models.CharField(blank=True, max_length=16, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('upi', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('coffee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='CafeApp.coffeevariety')),
            ],
        ),
        migrations.AddField(
            model_name='coffeevariety',
            name='sizes',
            field=models.ManyToManyField(related_name='coffee_varieties', to='CafeApp.size'),
        ),
        migrations.CreateModel(
            name='CoffeePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.coffeevariety')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.size')),
            ],
        ),
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.coffeevariety')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.size')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('coffee_varieties', models.ManyToManyField(related_name='stores', to='CafeApp.coffeevariety')),
            ],
        ),
    ]
