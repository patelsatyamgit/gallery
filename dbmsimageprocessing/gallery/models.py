from django.db import models

# Create your models here.
class Books(models.Model):
    imagename=models.CharField(max_length=20)
    image=models.ImageField(upload_to ='uploads/')
    def __str__(self):
        return self.imagename
