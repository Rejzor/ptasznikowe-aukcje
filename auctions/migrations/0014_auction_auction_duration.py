# Generated by Django 3.0.3 on 2020-02-14 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_remove_auction_highest_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auction_duration',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 21, 15, 47, 37, 164813)),
        ),
    ]
