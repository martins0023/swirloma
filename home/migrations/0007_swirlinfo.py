# Generated by Django 4.0.4 on 2022-09-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepost_service_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwirlInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('alternate_mobile_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('facebook_link', models.URLField(max_length=255)),
                ('instagram_link', models.URLField(max_length=255)),
                ('twitter_link', models.URLField(max_length=255)),
                ('linkedin_link', models.URLField(max_length=255)),
            ],
        ),
    ]