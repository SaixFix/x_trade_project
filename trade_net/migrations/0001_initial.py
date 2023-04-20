# Generated by Django 4.2 on 2023-04-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=100)),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('address', models.ManyToManyField(to='trade_net.address')),
                ('product', models.ManyToManyField(to='trade_net.product')),
            ],
            options={
                'verbose_name': 'Фабрика',
                'verbose_name_plural': 'Фабрики',
            },
        ),
    ]
