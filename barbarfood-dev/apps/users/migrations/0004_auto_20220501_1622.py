# Generated by Django 3.1.7 on 2022-05-01 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_address_usersession'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
    ]
