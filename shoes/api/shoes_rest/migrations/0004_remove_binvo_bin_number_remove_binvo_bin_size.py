# Generated by Django 4.0.3 on 2022-12-05 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0003_remove_binvo_bin_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binvo',
            name='bin_number',
        ),
        migrations.RemoveField(
            model_name='binvo',
            name='bin_size',
        ),
    ]
