# Generated by Django 5.0.6 on 2024-06-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
