from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DogToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    img = models.CharField(max_length=250)


    def __str__(self):
        return self.name


GENDER_CHOICES = (
	("f", "female"),
	("m", "male")
)

class Dog(models.Model):

    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #one to many

    dogtoys = models.ManyToManyField(DogToy)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


