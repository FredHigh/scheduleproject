# Generated by Django 4.1.7 on 2023-05-04 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('week_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=10)),
            ],
        ),
    ]
