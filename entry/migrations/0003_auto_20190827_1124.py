# Generated by Django 2.2.1 on 2019-08-27 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20190827_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ureg',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='ureg',
            old_name='Password',
            new_name='password',
        ),
    ]
