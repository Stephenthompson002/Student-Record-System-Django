# Generated by Django 5.0.3 on 2024-04-04 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srsapp', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(default='True', max_length=250)),
                ('subject2', models.CharField(default='True', max_length=250)),
                ('subject3', models.CharField(default='True', max_length=250)),
                ('subject4', models.CharField(default='True', max_length=250)),
                ('subject5', models.CharField(default='True', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srsapp.course')),
            ],
        ),
    ]
