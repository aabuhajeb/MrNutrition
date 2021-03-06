# Generated by Django 3.1.5 on 2021-05-04 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210503_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('ftype', models.CharField(choices=[('Salad', 'Salad'), ('Drinks', 'Drinks'), ('Protin', 'Protin'), ('Carbs', 'Carbs')], max_length=200, null=True)),
                ('size', models.CharField(choices=[('20g', '20g'), ('50g', '50g'), ('80g', '80g'), ('100g', '100g'), ('150g', '150g'), ('200g', '200g')], max_length=200, null=True)),
                ('manufacture', models.CharField(choices=[('Muscle Kitchen', 'Muscle Kitchen'), ('Thefitbar', 'Thefitbar'), ('Fit Food Factory', 'Fit Food Factory'), ('Calories Healthy Food Resturant', 'Calories Healthy Food Resturant'), ("OJ's - Super Fast Salads", "OJ's - Super Fast Salads")], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.food'),
        ),
    ]
