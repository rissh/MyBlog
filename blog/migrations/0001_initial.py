# Generated by Django 4.0.5 on 2022-06-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=140)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
