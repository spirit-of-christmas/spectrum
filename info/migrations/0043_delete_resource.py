# Generated by Django 4.2.15 on 2024-09-28 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0042_icalschedule_organisation"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Resource",
        ),
    ]