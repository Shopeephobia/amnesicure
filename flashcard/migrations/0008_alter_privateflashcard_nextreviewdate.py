# Generated by Django 4.1 on 2022-12-09 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0007_alter_privateflashcard_nextreviewdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateflashcard',
            name='nextReviewDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 19, 22, 5, 507945)),
        ),
    ]
