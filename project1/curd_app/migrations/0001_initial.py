# Generated by Django 5.0.4 on 2024-04-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.IntegerField()),
                ('product_quan', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=10)),
                ('delivery_address', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(choices=[('On', 'ONLINE'), ('COD', 'Cash on Delivery')], max_length=3)),
            ],
        ),
    ]