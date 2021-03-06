# Generated by Django 3.2 on 2021-05-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.FloatField()),
                ('r2', models.FloatField()),
                ('r3', models.FloatField()),
                ('g1', models.FloatField()),
                ('g2', models.FloatField()),
                ('g3', models.FloatField()),
                ('b1', models.FloatField()),
                ('b2', models.FloatField()),
                ('b3', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('testType', models.IntegerField()),
                ('degreeA', models.FloatField()),
                ('degreeB', models.FloatField()),
                ('degreeC', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
