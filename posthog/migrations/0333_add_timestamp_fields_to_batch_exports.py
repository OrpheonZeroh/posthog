# Generated by Django 3.2.18 on 2023-06-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0332_featureflag_has_enriched_analytics"),
    ]

    operations = [
        migrations.AddField(
            model_name="batchexport",
            name="end_at",
            field=models.DateTimeField(
                default=None, help_text="Time after which any Batch Export runs won't be triggered.", null=True
            ),
        ),
        migrations.AddField(
            model_name="batchexport",
            name="last_paused_at",
            field=models.DateTimeField(
                default=None, help_text="The timestamp at which this BatchExport was last paused.", null=True
            ),
        ),
        migrations.AddField(
            model_name="batchexport",
            name="start_at",
            field=models.DateTimeField(
                default=None, help_text="Time before which any Batch Export runs won't be triggered.", null=True
            ),
        ),
    ]
