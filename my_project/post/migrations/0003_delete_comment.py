# Generated by Django 3.1.5 on 2021-01-30 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210130_1445'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comment',
        ),
    ]
