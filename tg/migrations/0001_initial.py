# Generated by Django 4.0.2 on 2022-02-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('message', models.JSONField(default={'state': 0})),
            ],
        ),
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=256, null=True)),
                ('last_name', models.CharField(blank=True, max_length=256, null=True)),
                ('user_name', models.CharField(blank=True, max_length=256, null=True)),
                ('phone', models.ImageField(upload_to='')),
            ],
        ),
    ]
