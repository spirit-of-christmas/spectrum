# Generated by Django 4.2.13 on 2024-06-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0038_organisation_accepting_volunteers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="organisation",
            name="enable_scheduler",
            field=models.BooleanField(default=False),
        ),
    ]
