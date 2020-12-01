from django.db import models
from django.core.validators import URLValidator

class Question(models.Model):
    category=models.CharField(max_length=50)
    question=models.CharField(max_length=100)
    opt_1=models.CharField(max_length=50,)
    opt_2=models.CharField(max_length=50,)
    opt_3=models.CharField(max_length=50,)
    count_opt_1=models.IntegerField(default=0)
    count_opt_2=models.IntegerField(default=0)
    count_opt_3=models.IntegerField(default=0)
    ip_add=models.TextField(default=0)
    def __str__(self):
        return self.category
    def total(self):
        return self.count_opt_1+self.count_opt_2+self.count_opt_3    
    




   
    