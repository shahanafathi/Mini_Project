# Generated by Django 5.0.6 on 2024-05-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='DOB',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
