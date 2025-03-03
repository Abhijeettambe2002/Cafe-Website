# Generated by Django 5.1.5 on 2025-01-21 12:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CafeApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('card_num', models.CharField(blank=True, max_length=16, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('upi', models.CharField(blank=True, max_length=50, null=True)),
                ('sold_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.coffeevariety')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.size')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
