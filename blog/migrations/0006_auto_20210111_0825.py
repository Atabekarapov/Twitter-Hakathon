# Generated by Django 3.1.5 on 2021-01-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181024_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000000),
        ),
    ]
