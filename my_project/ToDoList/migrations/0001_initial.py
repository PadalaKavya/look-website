# Generated by Django 3.1.5 on 2021-04-25 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Deadline', models.DateField(default=datetime.date.today)),
                ('color', models.CharField(max_length=7, null=True)),
            ],
        ),
    ]
