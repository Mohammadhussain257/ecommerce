# Generated by Django 3.0.4 on 2020-04-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
