# Generated by Django 4.2.4 on 2023-08-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0011_alter_customerproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerproduct',
            name='category',
            field=models.CharField(choices=[('Automotive', 'Automotive'), ('Inverter', 'Inverter'), ('Tubular', 'Tubular')], max_length=100),
        ),
    ]
