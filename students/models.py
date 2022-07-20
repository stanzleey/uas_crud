from django.db import models

# Create your models here.
class Student(models.Model):
  nama = models.CharField(max_length=50)
  nip = models.PositiveIntegerField()
  devisi_pekerjaan = models.CharField(max_length=100)
  alamat = models.CharField(max_length=500)
  jenis_kelamin = models.CharField(max_length=100)

  def __str__(self):
    return f'Student: {self.nama}'
