# Generated by Django 4.2.6 on 2024-02-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='clip',
            field=models.CharField(default=models.TextField(), max_length=255),
        ),
    ]
