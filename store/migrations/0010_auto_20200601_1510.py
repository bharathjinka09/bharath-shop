# Generated by Django 3.0.5 on 2020-06-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200601_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_price',
            field=models.DecimalField(decimal_places=2, default='0.0  ', max_digits=7),
        ),
    ]
