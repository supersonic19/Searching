from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Expert(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length = 10 , validators=[MinLengthValidator])
    field = models.CharField(max_length = 100)
    

