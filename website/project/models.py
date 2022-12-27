from django.db import models

class daftarpasien(models.Model):
    Nama = models.CharField(max_length=30)
    Keluhan = models.CharField(max_length=100)
    Antrian = models.CharField(max_length=30)
    Dokter = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.Nama)


