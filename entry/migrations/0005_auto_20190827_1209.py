# Generated by Django 2.2.1 on 2019-08-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0004_auto_20190827_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='book_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='ticket_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
