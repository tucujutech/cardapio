from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=14, blank=False, null=False, unique= True)
    email = models.EmailField(unique=True)
    adress = models.TextField(null= False, blank= False)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return self.name
