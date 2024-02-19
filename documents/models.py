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

class Budget(models.Model):
    CHOICES = Category.objects.all().values_list('name','name') 
    titre = models.CharField(max_length = 1000)
    pdf = models.FileField(upload_to='pdfs/')
    category = models.CharField(max_length=300, choices = CHOICES, default='budget')
    #category = models.ForeignKey(Category, models.ForeignKey ,max_length=300, default='budget', choices = CHOICES)
 
    class Meta:
        ordering = ['titre']
     
    def __str__(self):
        return f"{self.titre}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Budget, self).save(*args, **kwargs)

class EtatBudget(models.Model):
    titre = models.CharField(max_length = 1000)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['titre']
     
    def __str__(self):
        return f"{self.titre}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(EtatBudget, self).save(*args, **kwargs)

class PlanPassation(models.Model):
    titre = models.CharField(max_length = 1000)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['titre']
     
    def __str__(self):
        return f"{self.titre}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(PlanPassation, self).save(*args, **kwargs)

# Nouveau

