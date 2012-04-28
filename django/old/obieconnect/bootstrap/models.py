from django.db import models

class ExampleFields(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name
        
class Course(models.Model):
    crn = models.IntegerField(max_length=5, blank=False)
    level = models.IntegerField(max_length=3, blank=False)
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=500)
    def __unicode__(self):
        return self.name