from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published = models.DateTimeField('published',default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project:project-detail',kwargs={'id':self.id})
