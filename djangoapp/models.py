from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name


class Post(models.Model):
    
    title=models.CharField(max_length=250)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


