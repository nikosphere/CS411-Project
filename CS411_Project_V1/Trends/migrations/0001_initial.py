# Generated by Django 2.2.6 on 2019-10-22 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trendSearch', models.CharField(max_length=250)),
                ('trendCategory', models.CharField(max_length=250)),
                ('trendLocation', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='YelpSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchParams', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trends.Trends')),
            ],
        ),
    ]
