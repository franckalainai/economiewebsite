from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
# Ajouter category

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
       return self.name

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('home')

class Social(models.Model):
    CHOICES = Category.objects.all().values_list('name','name') 
    direction_generale = models.CharField(max_length=100, blank=True)
    direction = models.CharField(max_length=1000, blank=True)
    titre = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=1000)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)
    category = models.CharField(max_length=300, choices = CHOICES, default='doem')
    #category = models.ForeignKey(Category, models.ForeignKey ,max_length=300, choices = CHOICES, default='DSPE')
 
    class Meta:
        ordering = ['titre']
     
    def __str__(self):
        return f"{self.titre}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Social, self).save(*args, **kwargs)