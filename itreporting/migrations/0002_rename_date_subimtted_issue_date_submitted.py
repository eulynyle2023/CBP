# Generated by Django 5.0.2 on 2024-03-10 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='date_subimtted',
            new_name='date_submitted',
        ),
    ]
