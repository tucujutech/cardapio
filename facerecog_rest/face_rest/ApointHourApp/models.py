from django.db import models

# Create your models here.
class Funcionario(models.Model):
    name = models.CharField(max_length=30, null= False, unique= True)
    rg = models.CharField(max_length=7, null= False, unique= True)
    cpf = models.CharField(max_length=11,  null=False , unique=True)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table= 'Funcionario'


class Apointment(models.Model):
    name_funcionario = models.ForeignKey(Funcionario, on_delete= models.CASCADE)
    hr_entry = models.TimeField(null= False)
    hr_exit = models.TimeField(null= False)

    def __str__(self):
        return self.hr_entry or self.hr_exit

    class Meta:
        db_table = 'Apointment'