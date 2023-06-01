# Generated by Django 4.2.1 on 2023-05-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='orderentry',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('processing', 'Processing'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], db_index=True, default='new', max_length=20, verbose_name='Status'),
        ),
    ]