# Generated by Django 4.1.2 on 2023-12-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographers', '0003_remove_portfolio_description_photographer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='price',
            field=models.IntegerField(default='100000'),
        ),
    ]