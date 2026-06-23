from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Record


# ======================== Formulario de Registro ========================
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        }),
        error_messages={
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Ingresa un correo electrónico válido, por ejemplo: nombre@dominio.com.',
        }
    )
    first_name = forms.CharField(
        label='',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre',
            'class': 'form-control'
        }),
        error_messages={
            'required': 'El nombre es obligatorio.',
            'max_length': 'El nombre no puede superar los 30 caracteres.',
        }
    )
    last_name = forms.CharField(
        label='',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellido',
            'class': 'form-control'
        }),
        error_messages={
            'required': 'El apellido es obligatorio.',
            'max_length': 'El apellido no puede superar los 30 caracteres.',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].widget.attrs['pattern'] = r'^[\w.@+-]+$'
        self.fields['username'].widget.attrs['data-error-pattern'] = 'Usa solo letras, dígitos y los símbolos @/./+/-/_.'
        self.fields['username'].label = ''
        self.fields['username'].error_messages.update({
            'required': 'El nombre de usuario es obligatorio.',
            'unique': 'Ya existe una cuenta con ese nombre de usuario.',
            'invalid': 'Usa solo letras, dígitos y los símbolos @/./+/-/_.',
        })
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.</small>'
            '</span>'
        )
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].error_messages.update({
            'required': 'La contraseña es obligatoria.',
        })
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
        self.fields['password2'].error_messages.update({
            'required': 'Debes confirmar la contraseña.',
        })
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Ingrese la misma contraseña.</small>'
            '</span>'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden. Verifica e intenta nuevamente.')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ya existe una cuenta registrada con este correo electrónico.')
        return email


# ======================== Formulario de Registros (Record) ========================
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El nombre es obligatorio.',
            'max_length': 'El nombre no puede superar los 50 caracteres.',
        }
    )
    last_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El apellido es obligatorio.',
            'max_length': 'El apellido no puede superar los 50 caracteres.',
        }
    )
    email = forms.EmailField(
        required=True,
        max_length=50,
        widget=forms.widgets.EmailInput(attrs={"placeholder": "Correo electrónico", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Ingresa un correo electrónico válido, por ejemplo: nombre@dominio.com.',
            'max_length': 'El correo no puede superar los 50 caracteres.',
        }
    )
    phone = forms.CharField(
        required=True,
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?\d{7,15}$',
            message='Teléfono inválido. Usa entre 7 y 15 dígitos, puede iniciar con "+" (ej: +573001234567).'
        )],
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Teléfono (ej: +573001234567)",
            "class": "form-control",
            "pattern": r"^\+?\d{7,15}$",
            "data-error-pattern": 'Teléfono inválido. Usa entre 7 y 15 dígitos, puede iniciar con "+" (ej: +573001234567).',
        }),
        label="",
        error_messages={
            'required': 'El teléfono es obligatorio.',
        }
    )
    Address = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'La dirección es obligatoria.',
            'max_length': 'La dirección no puede superar los 100 caracteres.',
        }
    )
    city = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'La ciudad es obligatoria.',
            'max_length': 'La ciudad no puede superar los 50 caracteres.',
        }
    )
    state = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Estado", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El estado/departamento es obligatorio.',
            'max_length': 'El estado no puede superar los 50 caracteres.',
        }
    )
    zipcode = forms.CharField(
        required=True,
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\d{4,10}$',
            message='Código postal inválido. Usa solo dígitos, entre 4 y 10 (ej: 110111).'
        )],
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Código postal (ej: 110111)",
            "class": "form-control",
            "pattern": r"^\d{4,10}$",
            "data-error-pattern": 'Código postal inválido. Usa solo dígitos, entre 4 y 10 (ej: 110111).',
        }),
        label="",
        error_messages={
            'required': 'El código postal es obligatorio.',
        }
    )

    class Meta:
        model = Record
        exclude = ("user",)


# ======================== Formulario de Actualización de Usuario ========================
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Nombre de usuario",
            "class": "form-control",
            "pattern": r"^[\w.@+-]+$",
            "data-error-pattern": "Usa solo letras, dígitos y los símbolos @/./+/-/_.",
        }),
        label="",
        error_messages={
            'required': 'El nombre de usuario es obligatorio.',
            'unique': 'Ya existe una cuenta con ese nombre de usuario.',
        }
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El nombre es obligatorio.',
        }
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El apellido es obligatorio.',
        }
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(attrs={"placeholder": "Correo electrónico", "class": "form-control"}),
        label="",
        error_messages={
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Ingresa un correo electrónico válido, por ejemplo: nombre@dominio.com.',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email__iexact=email)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError('Ya existe otra cuenta registrada con este correo electrónico.')
        return email