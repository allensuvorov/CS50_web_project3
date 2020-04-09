# Generated by Django 2.0.3 on 2020-04-09 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_name'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
