# Generated by Django 4.2.11 on 2024-05-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0037_organisation_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="organisation",
            name="accepting_volunteers",
            field=models.BooleanField(default=False),
        ),
    ]
