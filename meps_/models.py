from django.db import models
from django.utils.text import slugify

class Ministere(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=1000)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Ministere, self).save(*args, **kwargs)


