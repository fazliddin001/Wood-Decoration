# Generated by Django 5.0 on 2024-02-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_userfeedbackmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='text',
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
