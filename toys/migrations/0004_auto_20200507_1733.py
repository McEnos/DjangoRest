# Generated by Django 3.0.6 on 2020-05-07 14:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('toys', '0003_auto_20200507_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toy',
            old_name='release_data',
            new_name='release_date',
        ),
    ]