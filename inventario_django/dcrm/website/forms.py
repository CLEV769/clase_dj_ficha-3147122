# website/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Record


# ======================== Formulario de Registro ========================
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre',
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellido',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.</small>'
            '</span>'
        )
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Tu contraseña no puede ser demasiado similar a tu otra información personal.</li>'
            '<li>Tu contraseña debe contener al menos 8 caracteres.</li>'
            '<li>Tu contraseña no puede ser una contraseña común.</li>'
            '<li>Tu contraseña no puede ser completamente numérica.</li>'
            '</ul>'
        )
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Ingrese la misma contraseña.</small>'
            '</span>'
        )


# ======================== Formulario de Registros (Record) ========================
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Correo electrónico", "class": "form-control"}), label="")
    phone = forms.CharField(
        required=True,
        validators=[RegexValidator(
            regex=r'^\+?\d{7,15}$',
            message='Teléfono inválido. Debe tener entre 7 y 15 dígitos (puede iniciar con +).'
        )],
        widget=forms.widgets.TextInput(attrs={"placeholder": "Teléfono (ej: +573001234567)", "class": "form-control"}),
        label=""
    )
    Address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Estado", "class": "form-control"}), label="")
    zipcode = forms.CharField(
        required=True,
        validators=[RegexValidator(
            regex=r'^\d{4,10}$',
            message='Código postal inválido. Debe tener entre 4 y 10 dígitos numéricos.'
        )],
        widget=forms.widgets.TextInput(attrs={"placeholder": "Código postal (ej: 110111)", "class": "form-control"}),
        label=""
    )

    class Meta:
        model = Record
        exclude = ("user",)


# ======================== Formulario de Actualización de Usuario ========================
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre de usuario", "class": "form-control"}), label="")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder": "Correo electrónico", "class": "form-control"}), label="")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')