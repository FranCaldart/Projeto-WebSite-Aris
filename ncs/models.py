from django.db import models

# Create your models here.
import geocoder
# Create your models here.
class NC (models.Model):
    Municipio = models.CharField(max_length= 50)
    TN = models.CharField(max_length=20)
    Numero = models.CharField(max_length=20)
    Descricao = models.CharField(max_length=500, null= True)
    Unidade = models.CharField (max_length=200, null=True)
    Prazo = models.DateField(null=True)
    TipoSituacao = (
        ('Atendida','Atendida'),
        ('Pendente', 'Pendente'),

    )
    Situacao = models.CharField(max_length=20, choices=TipoSituacao, null=True)
    OBS = models.CharField(max_length=40, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    
    class Meta:
        verbose_name_plural = 'NC'
    def save(self,*args,**kwargs):
        self.latitude = geocoder.osm(self.Municipio).lat
        self.longitude = geocoder.osm(self.Municipio).lng
        return super().save(*args,**kwargs)
    
