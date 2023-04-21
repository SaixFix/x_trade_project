# Generated by Django 4.2 on 2023-04-21 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade_net', '0005_retailnetwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoleTrader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=100)),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade_net.address')),
                ('product', models.ManyToManyField(to='trade_net.product')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade_net.factory', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Индивидуальный предприниматель',
                'verbose_name_plural': 'Индивидуальный предприниматели',
            },
        ),
    ]