# Generated by Django 2.2.24 on 2021-07-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emeis_core", "0003_localized_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default="", max_length=128, verbose_name="password"),
            preserve_default=False,
        ),
    ]
