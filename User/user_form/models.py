from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name+' - '+self.date_of_birth+' - '+self.email+' - '+self.phone