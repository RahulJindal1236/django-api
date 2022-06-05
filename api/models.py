from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)