# Generated by Django 4.2.7 on 2024-01-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpoint',
            name='post_header',
            field=models.CharField(default='HEADER', max_length=250),
        ),
    ]
