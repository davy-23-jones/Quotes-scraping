from django.db import models

# Create your models here.
class Scrape(models.Model):
    quote = models.CharField()
    author = models.CharField()
    tags = models.CharField()
    
    def __str__(self):
        return f"{self.author}"