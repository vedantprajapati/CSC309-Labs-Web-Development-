# Generated by Django 4.1.3 on 2022-11-18 23:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_coach'),
        ('studios', '0004_alter_studio_address_alter_studio_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('keywords', models.JSONField(blank=True, null=True)),
                ('capacity', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('session_length', models.DurationField()),
                ('end_date', models.DateField(default=datetime.date(2022, 12, 18))),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='classes', to='users.coach')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='studios.studio')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('session_length', models.DurationField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('tfc_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_sessions', to='classes.class')),
            ],
            options={
                'verbose_name': 'ClassSession',
                'verbose_name_plural': 'ClassSessions',
            },
        ),
    ]