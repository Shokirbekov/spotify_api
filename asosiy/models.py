from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    tugilgan_sana = models.DateField()
    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom = models.CharField(max_length=100)
    sana = models.DateField(null=True, blank=True)
    rasm = models.URLField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Qoshiq(models.Model):
    nom = models.CharField(max_length=150)
    janr = models.CharField(max_length=150)
    davomiylik = models.DurationField()
    fayl = models.URLField()
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nom