from django.db import models

# Create your models here.


class Home(models.Model):
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return f'The Home at {self.street} in {self.city} costs ${self.price}'
