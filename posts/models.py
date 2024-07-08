from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30,null=False)
    created_by = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = "Catogories"

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category,null=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=False)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=200)
    created_by = models.DateTimeField(auto_now_add=True)



