# Generated by Django 2.2.7 on 2019-12-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(default=''),
        ),
    ]