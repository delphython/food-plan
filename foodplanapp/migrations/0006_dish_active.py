# Generated by Django 4.0.3 on 2022-03-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplanapp', '0005_merge_0002_delete_user_0004_alter_dish_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
    ]