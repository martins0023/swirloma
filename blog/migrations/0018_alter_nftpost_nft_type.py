# Generated by Django 4.0.4 on 2022-09-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_nftpost_nft_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftpost',
            name='nft_type',
            field=models.CharField(choices=[('collection', 'collection'), ('single', 'single')], max_length=100),
        ),
    ]
