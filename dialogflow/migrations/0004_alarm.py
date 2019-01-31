# Generated by Django 2.1 on 2018-09-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialogflow', '0003_bus_cancel_list_runningstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('card_id', models.IntegerField(blank=True)),
                ('time', models.IntegerField(blank=True)),
            ],
        ),
    ]
