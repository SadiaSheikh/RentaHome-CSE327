# Generated by Django 3.1.7 on 2021-04-26 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210426_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='number',
            new_name='phone',
        ),
    ]