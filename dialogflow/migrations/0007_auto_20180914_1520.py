# Generated by Django 2.1 on 2018-09-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialogflow', '0006_auto_20180914_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]