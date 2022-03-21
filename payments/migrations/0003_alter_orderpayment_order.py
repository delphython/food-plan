# Generated by Django 4.0.3 on 2022-03-21 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodplanapp', '0021_alter_order_options_alter_price_options_and_more'),
        ('payments', '0002_orderpaymentsummary_alter_orderpayment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpayment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='foodplanapp.order', verbose_name='Заказ к оплате'),
        ),
    ]