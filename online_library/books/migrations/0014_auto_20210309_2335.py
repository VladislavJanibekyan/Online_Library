# Generated by Django 3.1.6 on 2021-03-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20210309_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='rate_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]