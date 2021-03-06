# Generated by Django 4.0.3 on 2022-03-16 12:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='????????????????')),
                ('ingredients', models.TextField(verbose_name='??????????????????????')),
                ('image', models.ImageField(upload_to='', verbose_name='??????????????????????')),
                ('calories', models.IntegerField(verbose_name='????????????????????????, ????????')),
                ('weight', models.IntegerField(verbose_name='??????, ??')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.IntegerField(verbose_name='?????????? ????????????????, ??????')),
                ('meal', models.IntegerField(verbose_name='?????????????? ???? ???????????? ?????????? ????????, %')),
                ('new_year_menu', models.IntegerField(verbose_name='?????????????? ???? ???????????????????? ????????, %')),
                ('allergy', models.IntegerField(verbose_name='?????????????? ???? ?????????????????????????????? ????????, %')),
                ('promo_code', models.IntegerField(verbose_name='???????????? ???? ????????????????, %')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(choices=[(3, '3 ??????'), (12, '12 ??????')], verbose_name='???????? ????????????????, ??????')),
                ('breakfast', models.BooleanField(verbose_name='????????????????')),
                ('lunch', models.BooleanField(verbose_name='??????????')),
                ('dinner', models.BooleanField(verbose_name='??????????')),
                ('dessert', models.BooleanField(verbose_name='??????????????')),
                ('new_year_menu', models.BooleanField(verbose_name='???????????????????? ????????')),
                ('persons_amount', models.IntegerField(verbose_name='???????????????????? ????????????')),
                ('allergy1', models.BooleanField(verbose_name='???????????????? 1')),
                ('allergy2', models.BooleanField(verbose_name='???????????????? 2')),
                ('allergy3', models.BooleanField(verbose_name='???????????????? 3')),
                ('promo_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='????????????????')),
                ('total_price', models.IntegerField(verbose_name='?????????????????? ????????????????')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
        ),
    ]
