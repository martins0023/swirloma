# Generated by Django 4.0.4 on 2022-09-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_nftpost_nft_fixed_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftpost',
            name='nft_type',
            field=models.CharField(choices=[('single', 'single'), ('collections', 'collections')], max_length=100),
        ),
    ]