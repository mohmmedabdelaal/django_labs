# Generated by Django 4.0.1 on 2022-02-02 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itistudent', '0004_rename_name_forming_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
    ]
