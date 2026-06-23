# website/views.py
from .models import Record
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, UserUpdateForm
from django.contrib.auth.models import User, Group
from functools import wraps


# ======================== Decorador de Roles ========================
def role_required(*group_names):
    """Decorador que verifica si el usuario pertenece a uno de los grupos indicados."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, "Debes iniciar sesión para acceder a esta página.")
                return redirect('home')
            # Los superusuarios siempre tienen acceso
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            # Verificar si el usuario pertenece a alguno de los grupos requeridos
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            messages.error(request, "No tienes permisos suficientes para acceder a esta sección.")
            return redirect('home')
        return wrapper
    return decorator


# ======================== Vistas Públicas ========================
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "¡Has iniciado sesión exitosamente!")
            return redirect('home')
        else:
            messages.error(request, "Credenciales inválidas. Inténtalo de nuevo.")
            return redirect('home')
    else:
        records = Record.objects.all()
        return render(request, 'home.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "¡Has cerrado sesión exitosamente!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Asignar automáticamente al grupo "viewer"
            viewer_group, _ = Group.objects.get_or_create(name='viewer')
            new_user.groups.add(viewer_group)
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


# ======================== CRUD de Registros ========================
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "Debes iniciar sesión para ver este registro.")
        return redirect('home')


@role_required('admin', 'editor')
def delete_record(request, pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "El registro ha sido eliminado exitosamente.")
    return redirect('home')


@role_required('admin', 'editor')
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "El registro ha sido agregado exitosamente.")
            return redirect('home')
    return render(request, 'add_record.html', {'form': form})


@role_required('admin', 'editor')
def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "El registro ha sido actualizado exitosamente.")
        return redirect('home')
    return render(request, 'update_record.html', {'form': form})


# ======================== Gestión de Usuarios (solo admin) ========================
@role_required('admin')
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


@role_required('admin')
def user_detail(request, pk):
    user_info = User.objects.get(id=pk)
    return render(request, 'user_detail.html', {'user_info': user_info})


@role_required('admin')
def user_update(request, pk):
    current_user = User.objects.get(id=pk)
    form = UserUpdateForm(request.POST or None, instance=current_user)
    if form.is_valid():
        form.save()
        messages.success(request, "El usuario ha sido actualizado exitosamente.")
        return redirect('user_list')
    return render(request, 'user_update.html', {'form': form, 'user_info': current_user})


@role_required('admin')
def user_delete(request, pk):
    user_to_delete = User.objects.get(id=pk)
    user_to_delete.delete()
    messages.success(request, "El usuario ha sido eliminado exitosamente.")
    return redirect('user_list')


@role_required('admin')
def add_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El usuario ha sido creado exitosamente.")
            return redirect('user_list')
        else:
            messages.error(request, f"Error en el formulario: {form.errors}")
    else:
        form = SignUpForm()
    return render(request, 'add_user.html', {'form': form})
