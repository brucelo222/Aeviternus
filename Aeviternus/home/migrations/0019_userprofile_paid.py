# Generated by Django 2.0.4 on 2018-05-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20180501_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
