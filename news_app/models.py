from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null = True)
    publish_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

        
class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='categories')
    name=models.CharField(max_length=100, blank=True, null = True)
    
    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null = True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    news_title = models.CharField(max_length=264, verbose_name='Put a title', blank=True, null = True)
    description = RichTextUploadingField(blank=True, null = True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news_title

