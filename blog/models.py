from django.db import models
import time
from datetime import date
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField



# Create your models here.
class submitform(models.Model):
    topic= models.CharField(max_length=60)
    file=models.FileField(upload_to='blog/images')
    slug=models.SlugField(unique=True, max_length=255, null=True)
    content=models.TextField(blank=True)
    ck = RichTextField(blank=True,null=True)
    # subheading1=models.CharField(max_length=60,blank=True)
    # content1 = models.TextField(blank=True)
    # subheading2=models.CharField(max_length=60,blank=True)
    # content2 = models.TextField(blank=True)
    # subheading3=models.CharField(max_length=60,blank=True)
    # content3 = models.TextField(blank=True)
    # subheading4=models.CharField(max_length=60,blank=True)
    # content4 = models.TextField(blank=True)
    # subheading5=models.CharField(max_length=60,blank=True)
    # content5 = models.TextField(blank=True)
    # subheading6=models.CharField(max_length=60,blank=True)
    # content6 = models.TextField(blank=True)
    # subheading7=models.CharField(max_length=60,blank=True)
    # content7 = models.TextField(blank=True)
    # subheading8=models.CharField(max_length=60,blank=True)
    # content8 = models.TextField(blank=True)
    # subheading9=models.CharField(max_length=60,blank=True)
    # content9 = models.TextField(blank=True)
    # subheading10=models.CharField(max_length=60,blank=True)
    # content10 = models.TextField(blank=True)
    # subheading11=models.CharField(max_length=60,blank=True)
    # content11 = models.TextField(blank=True)
    # subheading12=models.CharField(max_length=60,blank=True)
    # content12 = models.TextField(blank=True)
    # subheading13=models.CharField(max_length=60,blank=True)
    # content13 = models.TextField(blank=True)
    # subheading14=models.CharField(max_length=60,blank=True)
    # content14 = models.TextField(blank=True)
    # subheading15=models.CharField(max_length=60,blank=True)
    # content15 = models.TextField(blank=True)
    # subheading16=models.CharField(max_length=60,blank=True)
    # content16 = models.TextField(blank=True)

# Create your models here.
    def __str__(self):
        return self.topic
    
class contactmdl(models.Model):
    name= models.CharField(max_length=60)
    email=models.FileField(upload_to='blog/images')
    contactprob=models.CharField(max_length=130)
# Create your models here.
    def __str__(self):
        return self.name
    
class topposts(models.Model):
    top_topic= models.CharField(max_length=60)
    top_file=models.FileField(upload_to='blog/images')
    top_slug=models.CharField(max_length=130)
    top_content = models.TextField()
    ck = RichTextField(blank=True,null=True)
    # top_subheading1=models.CharField(max_length=60,blank=True)
    # top_content1 = models.TextField(blank=True)
    # top_subheading2=models.CharField(max_length=60,blank=True)
    # top_content2 = models.TextField(blank=True)
    # top_subheading3=models.CharField(max_length=60,blank=True)
    # top_content3 = models.TextField(blank=True)
    # top_subheading4=models.CharField(max_length=60,blank=True)
    # top_content4 = models.TextField(blank=True)
    # top_subheading5=models.CharField(max_length=60,blank=True)
    # top_content5 = models.TextField(blank=True)
    # top_subheading6=models.CharField(max_length=60,blank=True)
    # top_content6 = models.TextField(blank=True)
    # top_subheading7=models.CharField(max_length=60,blank=True)
    # top_content7 = models.TextField(blank=True)
    # top_subheading8=models.CharField(max_length=60,blank=True)
    # top_content8 = models.TextField(blank=True)
    # top_subheading9=models.CharField(max_length=60,blank=True)
    # top_content9 = models.TextField(blank=True)
    # top_subheading10=models.CharField(max_length=60,blank=True)
    # top_content10 = models.TextField(blank=True)
    # top_subheading11=models.CharField(max_length=60,blank=True)
    # top_content11 = models.TextField(blank=True)
    # top_subheading12=models.CharField(max_length=60,blank=True)
    # top_content12 = models.TextField(blank=True)
    # top_subheading13=models.CharField(max_length=60,blank=True)
    # top_content13 = models.TextField(blank=True)
    # top_subheading14=models.CharField(max_length=60,blank=True)
    # top_content14 = models.TextField(blank=True)
    # top_subheading15=models.CharField(max_length=60,blank=True)
    # top_content15 = models.TextField(blank=True)
    # top_subheading16=models.CharField(max_length=60,blank=True)
    # top_content16 = models.TextField(blank=True)
# Create your models here.
    def __str__(self):
        return self.top_topic
    
