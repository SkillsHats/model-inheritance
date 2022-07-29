# Generated by Django 3.2 on 2022-07-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('pin_code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
