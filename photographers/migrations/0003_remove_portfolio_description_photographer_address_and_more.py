# Generated by Django 4.1.2 on 2023-12-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographers', '0002_alter_portfolio_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
        migrations.AddField(
            model_name='photographer',
            name='address',
            field=models.CharField(default='Your Default Address', max_length=200),
        ),
        migrations.AddField(
            model_name='photographer',
            name='contact_number',
            field=models.CharField(default='Your Default contact', max_length=20),
        ),
        migrations.AddField(
            model_name='photographer',
            name='email',
            field=models.EmailField(default='Your Default email', max_length=254),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='portfolio_images'),
        ),
    ]
