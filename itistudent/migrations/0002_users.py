# Generated by Django 4.0.1 on 2022-01-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itistudent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
