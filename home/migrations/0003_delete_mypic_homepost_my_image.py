# Generated by Django 4.0.4 on 2022-08-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_mypic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyPic',
        ),
        migrations.AddField(
            model_name='homepost',
            name='my_image',
            field=models.ImageField(default='me.jpg', upload_to='myimage'),
        ),
    ]
