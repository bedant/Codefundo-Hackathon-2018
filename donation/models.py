from django.db import models

# Create your models here.
class Donator(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    donationmade=models.IntegerField()
    
    def __str__(self):
        return "Rs "+str(self.donationmade)+" by "+str(self.name)