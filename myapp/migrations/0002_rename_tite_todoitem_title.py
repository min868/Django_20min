# Generated by Django 4.2.5 on 2023-09-24 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='tite',
            new_name='title',
        ),
    ]
