# Generated by Django 4.2.1 on 2023-06-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_orderentry_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='service/car_covers'),
        ),
    ]
