from django.db import models
from django.forms import CharField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    blog_image = models.ImageField(default='blog_image.jpg', upload_to='blog')
    
    def __str__(self):
        return self.blog_title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.blog_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (823, 800)
            img.thumbnail(output_size)
            img.save(self.blog_image.path)
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
    
class BlogDetail(models.Model):
    blog_welcome_intro = models.TextField(max_length=255)
    
    def __str__(self):
        return self.blog_welcome_intro
    
class NftPost(models.Model):
    nft_choices = choices = {
        ('single', 'single'),
        ('collection', 'collection')
    }
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    nft_title = models.CharField(max_length=100)
    nft_content = models.TextField()
    nft_more_content = models.TextField(default='')
    date_posted = models.DateTimeField(default=timezone.now)
    nft_image = models.ImageField(default='nft.jpg', upload_to='nfts')
    nft_type = models.CharField(max_length=100, choices = nft_choices)
    nft_fixed_price = models.FloatField(max_length=100, default=0.01)
    nft_old_price = models.FloatField(max_length=100, default=0.01)
    nft_external_link = models.URLField(max_length=255, default="")
    
    def __str__(self):
        return self.nft_title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.nft_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.nft_image.path)
    
    def get_absolute_url(self):
        return reverse('nft-detail', kwargs={'pk': self.pk})
    
class NftDetail(models.Model):
    nft_welcome_intro = models.TextField()
    about_nft = models.TextField()
    more_about_nft = models.TextField()
    
    def __str__(self):
        return self.nft_welcome_intro
    
class NftImage(models.Model):
    nft_title = models.CharField(max_length=100)
    nft_images = models.ImageField(default='nft-image.jpeg', upload_to='nft_images')
    
    def __str__(self):
        return self.nft_title