from django.db import models

class Todo(models.Model):
    tittle=models.CharField(max_length=100,unique=True,blank=False)
    def __str__(self):
        return self.tittle
