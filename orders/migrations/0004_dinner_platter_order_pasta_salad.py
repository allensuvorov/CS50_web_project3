# Generated by Django 3.0.5 on 2020-04-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200411_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now=True)),
                ('dinner_platters', models.ManyToManyField(blank=True, to='orders.Dinner_platter')),
                ('pastas', models.ManyToManyField(blank=True, to='orders.Pasta')),
                ('pizzas', models.ManyToManyField(blank=True, to='orders.Pizza')),
                ('subs', models.ManyToManyField(blank=True, to='orders.Sub')),
            ],
        ),
    ]
