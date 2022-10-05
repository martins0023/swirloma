# Generated by Django 4.0.4 on 2022-09-16 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_blogdetails_blogdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='NftImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nft_title', models.CharField(max_length=100)),
                ('nft_images', models.ImageField(default='nft-image.jpeg', upload_to='nft_images')),
            ],
        ),
        migrations.AlterField(
            model_name='nftdetail',
            name='about_nft',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='nftdetail',
            name='more_about_nft',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='nftdetail',
            name='nft_welcome_intro',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='nftpost',
            name='nft_type',
            field=models.CharField(choices=[('single', 'single'), ('collections', 'collections')], max_length=100),
        ),
    ]