from django.db import models

# Create your models here.
class Annotation(models.Model):
    x=models.FloatField()
    y=models.FloatField()
    msg=models.CharField(max_length=200)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.msg
    
class Login(models.Model):
    username=models.CharField(max_length=100) 
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.msg   