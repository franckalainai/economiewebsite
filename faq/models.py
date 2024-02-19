from django.db import models
from django.utils.text import slugify
# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    reponse = models.CharField(max_length=200)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Faq, self).save(*args, **kwargs)