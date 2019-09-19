from django.db import models

# Create your models here.
class Departamento(models.Model):
    nomeDepartamento = models.CharField(max_length=50, null = False,unique=True)
    #descricao = models.TextField(null=False)

    class Meta:
        db_table = 'Departamento'

    def __str__(self):
        return self.nomeDepartamento


class Funcao(models.Model):
    nomeFuncao = models.CharField(max_length=20, null = False, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Funcao'

    def __str__(self):
        return self.nomeFuncao