# Generated by Django 4.2.4 on 2023-09-04 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_cart_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
