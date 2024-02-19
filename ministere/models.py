from django.db import models
from django.utils.text import slugify
# Create your models here.
class Mission(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Mission, self).save(*args, **kwargs)


class Cabinet(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Cabinet, self).save(*args, **kwargs)

class Organigramme(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Organigramme, self).save(*args, **kwargs)

class Tutel(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    contact = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Tutel, self).save(*args, **kwargs)

class Ecole(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    contact = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Ecole, self).save(*args, **kwargs)


class Organisation(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Organisation, self).save(*args, **kwargs)


class Biographie(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Biographie, self).save(*args, **kwargs)
        
class Produit(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Produit, self).save(*args, **kwargs)