# Generated by Django 4.2.11 on 2024-05-12 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Company',
            new_name='company',
        ),
    ]
