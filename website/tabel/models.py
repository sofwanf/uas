from django.db import models


class pasien(models.Model):
    Nama = models.CharField(max_length=30)
    Keluhan = models.CharField(max_length=300)
    Antrian = models.CharField(max_length=10)
    Dokter = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.Nama)
