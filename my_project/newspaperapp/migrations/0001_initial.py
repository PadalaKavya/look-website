# Generated by Django 3.1.5 on 2021-01-30 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category_image', models.ImageField(upload_to='imgs')),
            ],
        ),
        migrations.CreateModel(
            name='newsmodel_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaperapp.category')),
            ],
        ),
    ]
