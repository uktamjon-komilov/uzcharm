# Generated by Django 3.2.5 on 2021-08-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettings',
            name='site_background',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Site Background'),
        ),
        migrations.AlterField(
            model_name='menusettings',
            name='site_background2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Site Background 2'),
        ),
    ]
