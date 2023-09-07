# Generated by Django 4.2.4 on 2023-09-04 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0017_alter_customerproduct_category'),
        ('customer', '0011_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.customerproduct', verbose_name='product ID')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user ID')),
            ],
        ),
    ]
