# Generated by Django 2.2.4 on 2019-08-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swabs', '0015_auto_20190827_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swab',
            name='HIVexposed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='swab',
            name='Presence_of_Pneumococcus',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
