# Generated by Django 4.2.7 on 2023-11-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_num',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_count',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
