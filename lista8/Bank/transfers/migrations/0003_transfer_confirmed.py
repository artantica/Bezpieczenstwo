# Generated by Django 2.2.7 on 2019-12-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0002_auto_20191117_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
