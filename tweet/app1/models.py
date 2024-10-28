from django.db import models

# Create your models here.
class tweeter(models.Model):
    person=models.CharField(max_length=50)
    dop=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=150)


    def __str__(self):
        return self.person
    

class Manufacturer(models.Model):
    brand=models.CharField(max_length=50)
    ceo=models.CharField(max_length=50)
    turnover=models.IntegerField()

    def __str__(self):
        return self.brand
    
class Car(models.Model):
    name=models.CharField(max_length=70)
    year=models.IntegerField()
    manufacture=models.ForeignKey('Manufacturer',on_delete=models.CASCADE)
    fuel=models.CharField(max_length=20)

    def __str__(self):
        return self.name