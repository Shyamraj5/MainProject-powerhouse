# Generated by Django 4.2.5 on 2023-10-07 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_alter_adminresponse_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminresponse',
            name='complaint',
        ),
    ]