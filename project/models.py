from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published = models.DateTimeField('published',default=datetime.now)
    #ticket = models.ManyToManyField('ticket.Ticket',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project:project-detail',kwargs={'id':self.id})

    class Meta:
        permissions = (("can_add_ticket","Adds a ticket"),
                        ('can_remove_ticket','Removes a ticket'),)
