# Generated by Django 3.1.5 on 2021-04-25 14:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Self care', max_length=400)),
                ('article', models.URLField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Challengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Challenge', models.CharField(max_length=500)),
                ('Why', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='detox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='morning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='night',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='skincare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='stressbusters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Problem', models.CharField(max_length=500)),
                ('Why', models.TextField(max_length=500)),
                ('Avoid', models.TextField(max_length=500)),
                ('Fix', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=250)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=10000)),
            ],
        ),
    ]
