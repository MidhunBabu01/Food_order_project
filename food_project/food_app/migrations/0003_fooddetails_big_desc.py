# Generated by Django 3.1.7 on 2021-06-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0002_fooddetails_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddetails',
            name='big_desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]