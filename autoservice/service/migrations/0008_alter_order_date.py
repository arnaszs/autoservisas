# Generated by Django 4.2.1 on 2023-05-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_service_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='date'),
        ),
    ]