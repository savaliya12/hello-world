# Generated by Django 4.1.7 on 2023-03-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0011_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]