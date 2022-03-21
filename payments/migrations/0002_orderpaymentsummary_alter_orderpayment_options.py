# Generated by Django 4.0.3 on 2022-03-21 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPaymentSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Отчёт по платежам',
                'verbose_name_plural': 'Отчеты по платежам',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('payments.orderpayment',),
        ),
        migrations.AlterModelOptions(
            name='orderpayment',
            options={'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
    ]
