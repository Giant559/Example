from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=200,default='Null')
    project = models.ForeignKey('project.Project',on_delete=models.CASCADE)
    description = models.TextField()
    published = models.DateTimeField('published',default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket:ticket-detail',kwargs={'id':self.id})

#    class Meta:
#        permissions = (("can_add_ticket","Adds a ticket"),
#                        ('can_remove_ticket','Removes a ticket'),)
