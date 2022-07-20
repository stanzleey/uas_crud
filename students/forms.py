from django import forms 
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['nama', 'nip', 'devisi_pekerjaan', 'alamat', 'jenis_kelamin']
    labels = {
      'nama': 'Nama', 
      'nip': 'NIP', 
      'devisi_pekerjaan': 'Devisi pekerjaan', 
      'alamat': 'Alamat', 
      'jenis_kelamin': 'Jenis kelamin'
    }
    widgets = {
      'nama': forms.TextInput(attrs={'class': 'form-control'}), 
      'nip': forms.NumberInput(attrs={'class': 'form-control'}),
      'devisi_pekerjaan': forms.TextInput(attrs={'class': 'form-control'}),
      'alamat': forms.TextInput(attrs={'class': 'form-control'}),
      'jenis_kelamin': forms.TextInput(attrs={'class': 'form-control'}),
    }