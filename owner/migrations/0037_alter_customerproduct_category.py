# Generated by Django 4.2.5 on 2024-02-14 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0036_alter_customerproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerproduct',
            name='category',
            field=models.CharField(choices=[('Tubular', 'Tubular'), ('Automotive', 'Automotive'), ('Inverter', 'Inverter')], max_length=100),
        ),
    ]
