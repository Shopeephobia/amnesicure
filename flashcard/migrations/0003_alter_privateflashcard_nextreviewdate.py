# Generated by Django 4.1 on 2022-12-05 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flashcard", "0002_privateflashcard_nextreviewdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="privateflashcard",
            name="nextReviewDate",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 5, 22, 35, 29, 757240)
            ),
        ),
    ]