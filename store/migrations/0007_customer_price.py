# Generated by Django 3.1.5 on 2021-05-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210504_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
