# Generated by Django 4.0.4 on 2022-08-20 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_mypic_homepost_my_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepost',
            name='my_image',
        ),
    ]