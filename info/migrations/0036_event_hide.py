# Generated by Django 4.2.11 on 2024-03-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0035_alter_organisation_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="hide",
            field=models.BooleanField(default=False),
        ),
    ]
