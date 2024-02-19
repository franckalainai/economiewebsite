from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Banner(models.Model):
    nom = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('add-banner')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Banner, self).save(*args, **kwargs)

class PhotoMinistre(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('add-photo')