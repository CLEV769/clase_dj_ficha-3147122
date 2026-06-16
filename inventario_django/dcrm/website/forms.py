#website/forms.py
# importacion de librerias y funciones para la creación de formularios en Django
from django import forms # para crear formularios en Django y sus campos.
from django.contrib.auth.forms import UserCreationForm # para crear un formulario de registro de usuarios basado en el modelo de usuario de Django.
from django.contrib.auth.models import User # para acceder al modelo de usuario de Django, que representa a los usuarios registrados en la base de datos.
##solicitudes dentro de la base de datos por que el formulario de registro de usuarios necesita verificar si el nombre de usuario ya existe en la base de datos.
# usando tecnologia  orm
#from .models import * # para importar todos los modelos definidos en el archivo models.py de la aplicación, lo que permite utilizarlos en la creación de formularios relacionados con esos modelos.
from .models import Record # para importar el modelo Record definido en el archivo models.py de la aplicación, lo que permite utilizarlo en la creación de formularios relacionados con ese modelo.#tipe ignore


# formulario de registro de usuarios personalizado que hereda de UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})) # campo de correo electrónico adicional para el formulario de registro de usuarios.


    # campos de primer nombre y apellido para el formulario de registro de usuarios.
    first_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) # campo de primer nombre para el formulario de registro de usuarios.
    last_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido'})) # campo de apellido para el formulario de registro de usuarios.
    class Meta:
        # atributos de la clase Meta para configurar el formulario de registro de usuarios.
        # La clase Meta se utiliza para configurar el formulario, especificando el modelo asociado y los campos que se incluirán en el formulario.
        model = User # especifica que el modelo asociado a este formulario es el modelo User de Django.
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') # campos que se incluirán en el formulario de registro de usuarios, incluyendo el nombre de usuario, primer nombre, apellido, correo electrónico y las contraseñas.
        # los metodos
       
        def __init__(self,*args, **kwargs) -> None:
            # *args y **kwargs son parámetros que permiten pasar un número variable de argumentos posicionales y de palabras clave al método __init__. Esto es útil para permitir flexibilidad en la inicialización del formulario, ya que puede aceptar diferentes conjuntos de argumentos según sea necesario.inicializa el formulario utilizando el constructor de la clase padre UserCreationForm y luego personaliza los atributos de los campos del formulario
            super(SignUpForm, self).__init__(*args, **kwargs) # llama al constructor de la clase padre para inicializar el formulario.
            self.fields['username'].widget.attrs['class'] = 'form-control' # personaliza el campo de nombre de usuario agregando la clase CSS 'form-control' para mejorar su apariencia en el formulario.
            self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario' # personaliza el campo de nombre de usuario agregando un marcador de posición para indicar al usuario qué información se espera en ese campo.
            self.fields['username'].label= '' # personaliza el campo de nombre de usuario eliminando la etiqueta del campo para una apariencia más limpia en el formulario.
            self.fields['username'].help_text=('<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.</small></span>') # personaliza el campo de nombre de usuario agregando un mensaje de ayuda para indicar al usuario los requisitos para el nombre de usuario.
            self.fields['password1'].widget.attrs['class'] = 'form-control' # personaliza el campo de contraseña 1 agregando la clase CSS 'form-control' para mejorar su apariencia en el formulario.
            self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña' # personaliza el campo de contraseña 1 agregando un marcador de posición para indicar al usuario qué información se espera en ese campo.
            self.fields['password1'].label= '' # personaliza el campo de contraseña 1 eliminando la etiqueta del campo para una apariencia más limpia en el formulario.
            self.fields['password1'].help_text=(
               
                '<ul class="form-text text-muted small">'
                '<li>Tu contraseña no puede ser demasiado similar a tu otra información personal.</li>'
                '<li>Tu contraseña debe contener al menos 8 caracteres.</li>'
                '<li>Tu contraseña no puede ser una contraseña común.</li>'
                '<li>Tu contraseña no puede ser completamente numérica.</li>'
                '</ul>'
            ) # personaliza el campo de contraseña 1 agregando un mensaje de ayuda para indicar al usuario los requisitos para la contraseña.
            #Personaliza el campo de contraseña 2
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Contraseña'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text=(
                '<span class= "form text text muted><small>'
                'Ingrese la misma contraseña.'
                '</small</span'
            )
#--------------------------Formulario para registro--------------------------------
#Formulario para agregar registro del modelo Records
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre","class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apellido","class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Correo electrónico","class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono","class":"form-control"}), label="")
    Address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Dirección","class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad","class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Estado","class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Código postal","class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)  # Excluye campos que no deben ser editados por el usuario