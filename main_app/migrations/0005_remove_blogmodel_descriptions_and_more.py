# Generated by Django 4.2 on 2024-02-16 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_blogmodel_feedbacks_feedbackmodel_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='blog',
        ),
        migrations.AddField(
            model_name='descriptionmodel',
            name='blogs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='main_app.blogmodel'),
        ),
        migrations.AddField(
            model_name='feedbackmodel',
            name='blogs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='main_app.blogmodel'),
        ),
    ]