# Generated by Django 5.0.3 on 2024-04-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_orderingtable_delete_order_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('rewards', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]