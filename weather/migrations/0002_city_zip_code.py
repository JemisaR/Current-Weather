# Generated by Django 2.2.1 on 2019-05-01 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='zip_code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]