# Generated by Django 4.0.4 on 2022-09-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_delete_blog_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_welcome_intro', models.TextField(max_length=255)),
            ],
        ),
    ]