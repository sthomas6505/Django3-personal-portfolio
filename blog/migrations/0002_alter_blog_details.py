# Generated by Django 3.2.9 on 2021-11-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='details',
            field=models.CharField(max_length=2500),
        ),
    ]