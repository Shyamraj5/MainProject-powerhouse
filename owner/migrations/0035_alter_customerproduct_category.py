# Generated by Django 4.2.5 on 2023-10-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0034_alter_customerproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerproduct',
            name='category',
            field=models.CharField(choices=[('Inverter', 'Inverter'), ('Tubular', 'Tubular'), ('Automotive', 'Automotive')], max_length=100),
        ),
    ]