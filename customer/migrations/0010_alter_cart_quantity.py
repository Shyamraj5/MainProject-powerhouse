# Generated by Django 4.2.4 on 2023-09-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_remove_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
