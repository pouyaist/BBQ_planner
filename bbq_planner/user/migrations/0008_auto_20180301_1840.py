# Generated by Django 2.0.2 on 2018-03-01 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_attendee_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='guests',
            new_name='number_of_guests',
        ),
    ]
