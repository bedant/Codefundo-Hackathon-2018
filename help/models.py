from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    name = models.CharField(max_length=25,null=True,blank=True)
    phone_number = models.CharField(max_length=10,null=True,blank=True)
    subject = models.CharField(max_length=120,null=True,blank=True)
    
    description = models.CharField(null=True,blank=True,max_length=1000)
    
    class Meta:
	
    #    model = Ticket
        verbose_name = 'Help Request'
        verbose_name_plural = 'Help Requests'
		
    def __str__(self):
        return "Help Request"
