# Generated by Django 2.1 on 2018-08-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
