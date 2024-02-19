from django.db import models

from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Zoom(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.titre

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('blog_detail')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Zoom, self).save(*args, **kwargs)
