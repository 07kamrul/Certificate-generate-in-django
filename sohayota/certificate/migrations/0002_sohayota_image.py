# Generated by Django 3.1.4 on 2020-12-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sohayota',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]