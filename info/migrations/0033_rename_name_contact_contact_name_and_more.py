# Generated by Django 4.2.10 on 2024-03-09 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0032_alter_event_tags_alter_resource_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='contact_name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='name',
            new_name='organisation_name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='name',
            new_name='region_name',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='name',
            new_name='resource_name',
        ),
    ]