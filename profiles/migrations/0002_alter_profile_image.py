# Generated by Django 5.1.3 on 2024-11-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_hcui3f', upload_to='images/'),
        ),
    ]
