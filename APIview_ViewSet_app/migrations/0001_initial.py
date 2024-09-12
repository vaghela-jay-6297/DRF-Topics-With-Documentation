# Generated by Django 5.0.6 on 2024-05-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=64)),
                ('smark', models.FloatField()),
                ('saddr', models.CharField(max_length=64)),
            ],
        ),
    ]