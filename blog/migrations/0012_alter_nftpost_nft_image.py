# Generated by Django 4.0.4 on 2022-09-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_nftimages_nftimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftpost',
            name='nft_image',
            field=models.ImageField(default='nft.jpg', upload_to='nfts'),
        ),
    ]
