# Generated by Django 2.2 on 2020-06-11 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0006_auto_20200611_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdb',
            old_name='user_name11',
            new_name='name',
        ),
    ]