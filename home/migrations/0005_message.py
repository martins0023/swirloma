# Generated by Django 4.0.4 on 2022-08-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_homepost_my_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Your name', max_length=200)),
                ('email_address', models.EmailField(default='Email address', max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
