# Generated by Django 2.1 on 2018-08-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_managers_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]