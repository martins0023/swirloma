# Generated by Django 4.0.4 on 2022-09-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_nftpost_nft_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftpost',
            name='nft_more_content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='nftpost',
            name='nft_type',
            field=models.CharField(choices=[('collection', 'collection'), ('single', 'single')], max_length=100),
        ),
    ]
