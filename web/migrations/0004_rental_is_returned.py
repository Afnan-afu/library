# Generated by Django 5.1.7 on 2025-03-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_user_rental_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
