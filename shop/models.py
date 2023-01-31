from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from django.urls import reverse

class categ(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])


class products(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name
