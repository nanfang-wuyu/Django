# Generated by Django 3.2 on 2021-05-25 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210525_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filters',
            old_name='userid',
            new_name='userId',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='userid',
            new_name='userId',
        ),
    ]
