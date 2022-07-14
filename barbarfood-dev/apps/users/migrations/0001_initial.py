# Generated by Django 3.1.7 on 2022-05-01 08:17

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='Моб. телефон')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('tdid', models.CharField(max_length=250, null=True, verbose_name='Юзер иденфикатор')),
                ('language', models.CharField(choices=[('kk', 'Казахский'), ('ru', 'Русский'), ('en', 'Английский')], default='ru', max_length=20, verbose_name='Язык')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('secret_key', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Секретный ключ')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Учетная запись',
                'verbose_name_plural': 'Учетная запись',
            },
        ),
    ]