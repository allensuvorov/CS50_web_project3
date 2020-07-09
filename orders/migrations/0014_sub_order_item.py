# Generated by Django 3.0.5 on 2020-07-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_sub_add_on_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('add_ons', models.ManyToManyField(blank=True, to='orders.Sub_add_on')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='orders.Order')),
                ('sub', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Sub')),
            ],
        ),
    ]
