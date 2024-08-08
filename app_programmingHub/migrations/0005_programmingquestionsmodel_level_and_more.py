# Generated by Django 5.0.6 on 2024-08-07 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_programmingHub', '0004_auto_20240807_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingquestionsmodel',
            name='level',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], default='Easy', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='submissionmodel',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='app_programmingHub.programmingquestionsmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submissionmodel',
            name='status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('Attempted', 'Attempted'), ('UnSolved', 'Unsolved')], default='UnSolved', max_length=30, null=True),
        ),
    ]
