# Generated by Django 5.0.6 on 2024-06-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0010_competetionmodel_alter_internshipmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competetionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='opportunities/competetion'),
        ),
        migrations.AlterField(
            model_name='internshipmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='opportunities/internships'),
        ),
    ]
