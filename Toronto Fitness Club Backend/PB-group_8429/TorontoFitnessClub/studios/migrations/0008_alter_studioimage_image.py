# Generated by Django 4.1.3 on 2022-11-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0007_remove_studio_avatar_remove_studioimage_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studioimage',
            name='image',
            field=models.ImageField(upload_to='images/studios/'),
        ),
    ]