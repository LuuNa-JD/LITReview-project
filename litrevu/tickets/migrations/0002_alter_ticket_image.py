# Generated by Django 5.1.1 on 2024-10-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ticket_images/'),
        ),
    ]
