# Generated by Django 2.2.5 on 2020-02-15 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_allbids'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllBids',
            new_name='BidsHistory',
        ),
    ]