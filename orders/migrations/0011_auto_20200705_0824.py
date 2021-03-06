# Generated by Django 3.0.5 on 2020-07-05 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200702_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_platter_size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='dinner_platter',
            name='size',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='orders.Dinner_platter_size'),
            preserve_default=False,
        ),
    ]
