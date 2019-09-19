from django.db import models

# Create your models here.
from django.db import models

from organizacionalApp.models import Departamento, Funcao


class Colaborador(models.Model):
    nome = models.CharField(max_length=60, null=False, unique=True)
    nascimento = models.DateField(null=False)
    rg = models.CharField(max_length=12, null=False)
    cpf = models.CharField(max_length=12, null=False)
    telefone = models.CharField(max_length=13, null=False)
    cnh = models.CharField(max_length=12)
    cnh_tipo = models.CharField(max_length=12,default='Não Possui', null=False)

    #sexo_choices = (
     #   ('M', 'M'),
      #  ('F', 'F'),
    #)
    sexo_choices = models.CharField(max_length=2, null=False)

    departamento = models.ForeignKey(Departamento , on_delete=models.CASCADE, to_field='nomeDepartamento')

    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, to_field='nomeFuncao')

    foto_colaborador = models.BinaryField(max_length=None, editable=True)

    class Meta:
        db_table = 'Colaborador'

    def __str__(self):
        return self.nome


class TipoFormacao(models.Model):
    tipo_formacao = models.CharField(max_length=13, null=False, unique=True)

    class Meta:
        db_table = 'Tipo_Formacao'

    def __str__(self):
        return self.tipo_formacao


class Formacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=False, to_field='nome')

    # tipo_choices = (
    #   ('Graduação','Graduação'),
    #   ('Pós-Graduação','Pós-Graduação'),
    #   ('Mestrado','Mestrado'),
    #   ('Doutorado','Doutorado'),
    #   ('Extensão','Extensão'),
    #   ('Certificação','Certificação')
    # )

    tipo_formacao = models.ForeignKey(TipoFormacao, on_delete=models.CASCADE, null=False,to_field='tipo_formacao')
    nome_curso = models.CharField(max_length=50, null=False)
    instituicao = models.CharField(max_length=50, null=False)
    dt_inicio = models.DateField(null=False)
    dt_termino = models.DateField(null=False)

    class Meta:
        db_table = 'Formacao'

    def __str__(self):
        return self.nome_curso


