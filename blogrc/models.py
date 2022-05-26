from django.db import models
from .helpers import *
# Create your models here.


CATEGORY_CHOICES = (
    ("P", "PROGRAMING"),
    ("PR", "PROJECT"),
    ("GM", "GAME"),
)
SUB_CATEGORY_CHOICES = (
    ("C", "C"),
    ("CPP", "CPP"),
    ("JV", "JAVA"),
    ("PY", "PYTHON"),
    ("FL", "FLUTTER"),
    ("GME", "GAME"),
)
class BlogModel(models.Model):
    banner = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    # user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, max_length=3) 
    content1 = models.TextField(null=True , blank=True)
    contentcode1 = models.TextField(null=True , blank=True)
    image1 = models.ImageField(upload_to='blog')
    content2 = models.TextField(null=True , blank=True)
    contentcode2 = models.TextField(null=True , blank=True)
    image2 = models.ImageField(upload_to='blog')
    content3 = models.TextField(null=True , blank=True)
    contentcode3 = models.TextField(null=True , blank=True)
    image3 = models.ImageField(upload_to='blog')
    contentkesimpulan = models.TextField(null=True , blank=True)
    link1 = models.CharField(max_length=1000, default="",null=True , blank=True)
    link2 = models.CharField(max_length=1000, default="",null=True , blank=True)
    link3 = models.CharField(max_length=1000, default="",null=True , blank=True)
    created_by = models.CharField(max_length=1000, default="",null=True , blank=True)
    contentvidio = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)


class BlogProjectModel(models.Model):
    banner = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    # user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, max_length=3) 
    content1 = models.TextField(null=True , blank=True)
    contentcode1 = models.TextField(null=True , blank=True)
    image1 = models.ImageField(upload_to='blog')
    content2 = models.TextField(null=True , blank=True)
    contentcode2 = models.TextField(null=True , blank=True)
    image2 = models.ImageField(upload_to='blog')
    content3 = models.TextField(null=True , blank=True)
    contentcode3 = models.TextField(null=True , blank=True)
    image3 = models.ImageField(upload_to='blog')
    contentkesimpulan = models.TextField(null=True , blank=True)
    link1 = models.CharField(max_length=1000, default="")
    link2 = models.CharField(max_length=1000)
    link3 = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=1000)
    contentvidio = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

    
# class fileblog(models.Model):
#     title = models.ForeignKey(BlogModel)
#     link1 = models.CharField(max_length=1000, null=True, blank=True)
#     link2 = models.CharField(max_length=1000, null=True, blank=True)
#     link3 = models.CharField(max_length=1000, null=True, blank=True)

    
    
    

