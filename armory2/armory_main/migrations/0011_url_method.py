# Generated by Django 3.1a1 on 2020-06-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armory_main', '0010_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='method',
            field=models.CharField(default='get', max_length=32),
        ),
    ]
