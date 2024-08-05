# Generated by Django 5.0.6 on 2024-08-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_courses', '0004_pythonmcqmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSSMCQModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=250)),
                ('option1', models.CharField(max_length=250)),
                ('option2', models.CharField(max_length=250)),
                ('option3', models.CharField(max_length=250)),
                ('option4', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=250)),
            ],
        ),
    ]
