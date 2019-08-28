from django.db import models

# Create your models here.

class Veterinario(models.Model):
    Nome= models.CharField(null= False, max_length= 30)
    CPF= models.CharField(null= False, max_length=14)
    CRMV= models.CharField(null= False, max_length=20)

    def __str__(self):
        return  self.Nome

    class Meta:
        db_table='Veterinario'


class Cliente(models.Model):
    Nome=models.CharField(null= False, max_length=30)
    CPF=models.CharField(null= False, max_length=14)
    Telefone=models.CharField(null= False, max_length=11)
    Endereco= models.TextField(null= False, max_length=100)

    def __str__(self):
        return  self.Nome

    class Meta:
        db_table='Cliente'


class Paciente(models.Model):
     Nome=models.CharField(null= False, max_length=30)
     Tipo=models.CharField(null= False, max_length=20)
     Raca=models.CharField(null= False, max_length=20)
     Idade=models.IntegerField()
     Peso=models.FloatField(null= False)
     Nome_Dono_Cliente=models.ForeignKey(Cliente,models.CASCADE)

     def __str__(self):
         return self.Nome

     class Meta:
         db_table='Paciente'

class Procedimento(models.Model):
     Nome_Procedimento=models.CharField(null= False, max_length=40)

     def __str__(self):
         return  self.Nome_Procedimento

     class Meta:
         db_table='Procedimento'

class AcaoProcedimento(models.Model):
    Procedimento=models.ForeignKey(Procedimento,models.CASCADE, null=False)
    Paciente=models.ForeignKey(Paciente,models.CASCADE, null=False)
    Veterinario=models.ForeignKey(Veterinario, models.CASCADE, null=False)
    Descricao_Procedimento=models.TextField(null= False, max_length=100)
    OBS=models.TextField(max_length=100)

    class Meta:
        db_table='Acao_Procedimento'

class Medicamento(models.Model):
    Nome_Medicamento=models.CharField(null=False, max_length=30)
    Tipo=models.CharField(null= False, max_length=30)
    Peso_Volume=models.FloatField(null=False)

    def __str__(self):
        return  self.Nome_Medicamento

    class Meta:
        db_table='Medicamento'

class Estoque(models.Model):
    Medicamento=models.ForeignKey(Medicamento,models.CASCADE)
    Quantidade=models.IntegerField(null=False)
    Validade=models.DateField(null=False)

    class Meta:
        db_table='Estoque'

#criar tabela de estoque, será necessário fazer uma procedure para interagir com o banco para aumentar ou diminuir a quantidade
#a medida que o for informado no sistema o uso ou a reposição no estoque.


