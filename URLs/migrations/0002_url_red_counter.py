# Generated by Django 4.0.6 on 2022-08-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='red_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
