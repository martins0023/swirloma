# Generated by Django 4.0.4 on 2022-09-16 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_blogdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='NftDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nft_welcome_intro', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NftPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nft_title', models.CharField(max_length=100)),
                ('nft_content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('nft_image', models.ImageField(default='blog_image.jpg', upload_to='blog')),
                ('nft_type', models.CharField(choices=[('single', 'single'), ('collections', 'collections')], max_length=100)),
                ('author', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]