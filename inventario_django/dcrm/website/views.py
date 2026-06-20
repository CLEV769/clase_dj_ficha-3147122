# Importa la función render, que permite combinar una plantilla HTML con datos y devolver una respuesta HTTP.
#website/views.py
from .models import Record # Importa el modelo Record definido en models.py, que representa los registros de clientes en la base de datos.
from django.shortcuts import render, redirect
# Importa el modelo User de Django, que representa a los usuarios en la base de datos.


# Importa funciones para autenticación de usuarios:
# - authenticate: verifica credenciales.
# - login: inicia sesión.
# - logout: cierra sesión.
from django.contrib.auth import authenticate, login, logout


# Importa el sistema de mensajes de Django para mostrar notificaciones al usuario.
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, UserUpdateForm # Importa los formularios personalizados definidos en forms.py.
from django.contrib.auth.models import User # Importa el modelo User de Django para gestión de usuarios.


# Aquí se deben crear las vistas de la aplicación.
# Esta función define la vista principal (home) del sitio.
def home(request):
    # Renderiza la plantilla 'home.html' y la retorna como respuesta HTTP.
    # No se pasan datos adicionales al contexto (diccionario vacío).
    if request.method == 'POST':
        # Si el método de la solicitud es POST, significa que se está enviando un formulario.
        # Aquí puedes manejar la lógica del formulario, como la autenticación de usuarios.
        username = request.POST['username'] # Obtiene el nombre de usuario del formulario.
        # Obtiene la contraseña del formulario.
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)# Verifica las credenciales del usuario.
        # Si el usuario es autenticado correctamente, se inicia sesión.
        if user is not None: # Si el usuario es autenticado correctamente.
            login(request, user)# Inicia sesión.
            # Muestra un mensaje de éxito al usuario.
            messages.success(request, "You Have Been Logged In!")# # Muestra un mensaje de éxito al usuario.
            return redirect('home')
        else:
            # Si las credenciales son incorrectas, se muestra un mensaje de error.
            messages.error(request, "Invalid Credentials!")
            # Muestra un mensaje de error al usuario.
            return redirect('home')
    else:
        # Si el método de la solicitud no es POST, simplemente renderiza la plantilla 'home.html'.
        records = Record.objects.all()
        return render(request, 'home.html', {'records': records}) # Renderiza la plantilla 'home.html' y pasa todos los registros de clientes al contexto.
# Esta función define la vista de inicio de sesión (login) del sitio.

def login_user(request):
    pass
def logout_user(request): # el cerrar sesesión (logout) del sitio.
    logout(request) # Cierra la sesión del usuario.
    messages.success(request, "You Have Been Logged Out!") # Muestra un mensaje de éxito al usuario.
    return redirect('home') # Redirige a la página principal (home).


def register_user(request):# Esta función define la vista de registro de usuarios (register) del sitio.
    # Si el método de la solicitud es POST, significa que se está enviando el formulario de registro.
    if request.method == 'POST':
        form = SignUpForm(request.POST) # Crea una instancia del formulario de registro con los datos enviados.
        if form.is_valid(): # Verifica si el formulario es válido.
            form.save() # Guarda el nuevo usuario en la base de datos.
            username = form.cleaned_data['username'] # Obtiene el nombre de usuario del formulario.
            password = form.cleaned_data['password1'] # Obtiene la contraseña del formulario.
            user = authenticate(username=username, password=password) # Autentica al nuevo usuario.
            login(request, user) # Inicia sesión para el nuevo usuario.
            messages.success(request, "You Have Registered!") # Muestra un mensaje de éxito al usuario.
            return redirect('home') # Redirige a la página principal (home).
    else:
        form = SignUpForm() # Si el método de la solicitud no es POST, crea una instancia vacía del formulario de registro.
    return render(request, 'register.html', {'form':form}) # Renderiza la plantilla 'register.html' y la retorna como respuesta HTTP.

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Usuario no autentificado")
        return redirect ('home') 

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "El registro ha sido eliminado exitosamente")
        return redirect('home')
    else:
        messages.success(request, "No estas autenticado para realizar esta accion")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record= form.save()
                messages.success(request,"Ya el registro fue agregado")
                return redirect('home')
        return render (request,'add_record.html',{'form': form})
    else:
        messages.success(request,"No estas autenticado entonces no se puede realizar esta accion")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Ya esta actualizando los datos")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'Error del usuario')
        return redirect ('home')

# ======================== Gestión de Usuarios ========================

def user_list(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})
    else:
        messages.success(request, "No estás autenticado para ver esta página")
        return redirect('home')

def user_detail(request, pk):
    if request.user.is_authenticated:
        user_info = User.objects.get(id=pk)
        return render(request, 'user_detail.html', {'user_info': user_info})
    else:
        messages.success(request, "No estás autenticado para ver esta página")
        return redirect('home')

def user_update(request, pk):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=pk)
        form = UserUpdateForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, "El usuario ha sido actualizado exitosamente")
            return redirect('user_list')
        return render(request, 'user_update.html', {'form': form, 'user_info': current_user})
    else:
        messages.success(request, "No estás autenticado para realizar esta acción")
        return redirect('home')

def user_delete(request, pk):
    if request.user.is_authenticated:
        user_to_delete = User.objects.get(id=pk)
        user_to_delete.delete()
        messages.success(request, "El usuario ha sido eliminado exitosamente")
        return redirect('user_list')
    else:
        messages.success(request, "No estás autenticado para realizar esta acción")
        return redirect('home')

def add_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "El usuario ha sido creado exitosamente")
                return redirect('user_list')
            else:
                # Muestra exactamente qué campo falló y por qué
                messages.error(request, f"Error en el formulario: {form.errors}")
        else:
            form = SignUpForm()
        return render(request, 'add_user.html', {'form': form})
    else:
        messages.error(request, "No estás autenticado para realizar esta acción")
        return redirect('home')
