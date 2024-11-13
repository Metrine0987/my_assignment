from django.db import models

# Create your models here.
class contacts(models.Model):
    """Contacts table"""
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.name