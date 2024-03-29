# Generated by Django 5.0 on 2024-02-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_servicecategories_servicecategorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUserEmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Subscribed Email',
                'verbose_name_plural': 'Subscribed Emails',
            },
        ),
    ]
