# Generated by Django 4.0.1 on 2022-02-02 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itistudent', '0003_forming'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forming',
            old_name='name',
            new_name='username',
        ),
    ]
