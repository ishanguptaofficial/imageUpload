# Generated by Django 3.1.6 on 2023-09-15 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210602_2010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
    ]
