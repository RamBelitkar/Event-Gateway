from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name
