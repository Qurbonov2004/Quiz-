# Generated by Django 5.0.2 on 2024-02-25 15:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_quiz_owner_delete_test_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
