# Generated by Django 4.2 on 2023-04-21 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade_net', '0003_alter_factory_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade_net.address'),
        ),
    ]
