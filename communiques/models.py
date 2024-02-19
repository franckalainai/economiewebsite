from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Communique(models.Model):
    titre = models.CharField(max_length = 1000)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['titre']
     
    def __str__(self):
        return f"{self.titre}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Communique, self).save(*args, **kwargs)