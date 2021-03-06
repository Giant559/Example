# Generated by Django 3.0.3 on 2020-03-11 21:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0004_auto_20200311_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('published', models.DateTimeField(default=datetime.datetime.now, verbose_name='published')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
    ]
