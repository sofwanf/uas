from django.forms import ModelForm
from .models import daftarpasien

class formdaftar(ModelForm):
    class Meta:
        model = daftarpasien
        fields = '__all__'
