# Generated by Django 5.2.4 on 2025-07-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='student_batch',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='relation',
            name='teacher_status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
