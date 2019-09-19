from django.db import models, connection

# Create your models here.
from core.models import Colaborador


class HoraExtra(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null= False, to_field='nome')
    data = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fim = models.TimeField(null= False)
    faturado = models.BooleanField(null=False)


    class Meta:
        db_table = 'HoraExtra'

    def __str__(self):
        return self.colaborador

    # This method counts the extra hours that are still active, or be, those who aren´t invoiced
    def CountHoraExtraNaoFaturada(self, colaborador):

        with connection.cursor() as cursor:
            cursor.execute('select count(t.data) from public."HoraExtra" t where t.colaborador_id = '
                           '(select id from public."Colaborador" where nome = %s) and t.faturado = false', [colaborador])
            row = cursor.fetchone()
        return row[0]

    # This method limits the quantity of extra hours registered by month
