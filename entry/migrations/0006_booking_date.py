# Generated by Django 2.2.1 on 2019-08-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0005_auto_20190827_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
