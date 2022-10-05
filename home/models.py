from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class ProjectPost(models.Model):
    project_title = models.CharField(max_length=100)
    project_content = models.TextField()
    project_media = models.FileField(upload_to="project_medias", default="project.mp4")
    project_file = models.FileField(upload_to='project_files')
    
    def __str__(self):
        return self.project_title

class HomePost(models.Model):
    service_title = models.CharField(max_length=100)
    service_content = models.TextField()
    service_files = models.FileField(upload_to="service_details_files", default="marketing.mp4")
    
    
    def __str__(self):
        return self.service_title
    
    
class Message(models.Model):
    full_name = models.CharField(max_length=200, default="Your name")
    email_address = models.EmailField(max_length=200, default="Email address")
    message = models.TextField()
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
class SwirlInfo(models.Model):
    email_address = models.EmailField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    alternate_mobile_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=255)
    instagram_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    whatsapp_link = models.URLField(max_length=255, default='link')
    upwork_link = models.URLField(max_length=255, default='link')
    fiverr_link = models.URLField(max_length=255, default='link')
    
    def __str__(self):
        return self.email_address
    

def set_time():
    from datetime import datetime
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"date and time in for is: ",dt_string)
    
    dt_hour = now.strftime("%H:%M:%S ")
    print(dt_hour)