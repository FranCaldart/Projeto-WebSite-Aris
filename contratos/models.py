from django.db import models

# Create your models here.

class Municipio(models.Model):
	municipio = models.CharField(max_length = 50)
	opcoes = [('Contrato de Programa', 'Contrato de Programa'), ('Contrato de Concessão','Contrato de Concessão')]
	instrumento_contratual = models.CharField(max_length = 50, choices=opcoes, null=True)
	def __str__(self):
		return self.municipio


class MetaSAA(models.Model):
	municipio = models.ForeignKey(Municipio, null= True, on_delete = models.CASCADE)
	meta = models.CharField(max_length = 500)
	Prazo = models.DateField(null=True)

class MetaSES(models.Model):
	municipio = models.ForeignKey(Municipio, null= True, on_delete = models.CASCADE)
	meta = models.CharField(max_length = 500)
	Prazo = models.DateField(null=True)