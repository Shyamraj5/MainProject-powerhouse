# Generated by Django 4.2.5 on 2023-10-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0024_alter_adminresponse_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminresponse',
            name='response',
            field=models.CharField(choices=[('thank you for your response', 'thank you for your response'), ('service engineer on the way', 'service engineer on the way'), ('having some delay come after a day', 'having some delay come after a day')], max_length=500),
        ),
    ]
