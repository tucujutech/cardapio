#teste de extração de dados de um pdf usando tabula
import tabula

j=tabula.read_pdf("/home/philipe/Documentos/Tiny - DANFE.pdf",multiple_tables=True)

print(j)