from django.db import models
from django.core.validators import RegexValidator

# Validadores Regex
phone_validator = RegexValidator(
    regex=r'^\+?\d{7,15}$',
    message='Teléfono inválido. Debe tener entre 7 y 15 dígitos (puede iniciar con +).'
)

zipcode_validator = RegexValidator(
    regex=r'^\d{4,10}$',
    message='Código postal inválido. Debe tener entre 4 y 10 dígitos numéricos.'
)

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    Address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20, validators=[zipcode_validator])
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")