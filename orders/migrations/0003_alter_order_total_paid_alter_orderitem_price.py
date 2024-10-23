# Generated by Django 5.1.2 on 2024-10-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_paid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]