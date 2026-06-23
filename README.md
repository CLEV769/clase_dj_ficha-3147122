# 🚀 Django CRM

Sistema CRM (Customer Relationship Management) desarrollado con Django y MySQL para la gestión de clientes y usuarios mediante un sistema de roles, interfaz moderna en modo oscuro y navegación dinámica.

---

## 📌 Características

- ✅ Gestión de clientes (CRUD completo)
- ✅ Gestión de usuarios
- ✅ Sistema de roles y permisos
- ✅ Autenticación segura con Django
- ✅ Validaciones mediante expresiones regulares (Regex)
- ✅ Interfaz moderna Dark Theme
- ✅ Notificaciones Toast
- ✅ Navegación SPA parcial con JavaScript
- ✅ Protección CSRF
- ✅ Variables de entorno mediante dotenv

---

## 🛠 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| Python | Lenguaje principal |
| Django 5.0.14 | Framework Backend |
| MySQL | Base de datos |
| Bootstrap 5 | Diseño responsive |
| HTML5 | Estructura |
| CSS3 | Estilos personalizados |
| JavaScript | Interactividad |
| python-dotenv | Variables de entorno |

---

## 📂 Estructura del Proyecto

```bash
dcrm/
│
├── manage.py
├── .env
├── .env.example
│
├── dcrm/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── website/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── templates/
    └── static/
```

---

## 👥 Sistema de Roles

El proyecto utiliza grupos de Django para controlar el acceso a las funcionalidades.

### 🔴 Admin

- Gestionar registros
- Gestionar usuarios
- Acceso total al sistema

### 🟡 Editor

- Crear registros
- Editar registros
- Eliminar registros

### 🔵 Viewer

- Solo lectura de registros

---

## 📊 Modelo Principal

### Record

```python
class Record(models.Model):
    first_name
    last_name
    email
    phone
    address
    city
    state
    zipcode
```

Permite almacenar la información de cada cliente registrado en el sistema.

---

## 🔐 Seguridad

- Contraseñas validadas por Django
- Protección CSRF
- Variables sensibles almacenadas en `.env`
- Sesiones protegidas
- Control de acceso por roles

---

## 🎨 Interfaz de Usuario

### Características Visuales

- Tema oscuro moderno
- Diseño responsive
- Badges de rol
- Tablas personalizadas
- Formularios estilizados
- Alertas Toast dinámicas

---

## ⚡ Navegación SPA

La aplicación implementa navegación parcial SPA utilizando:

```javascript
fetch()
history.pushState()
popstate
```

Esto permite una experiencia más fluida sin recargar completamente la página.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/django-crm.git
```

### 2. Entrar al proyecto

```bash
cd django-crm
```

### 3. Crear entorno virtual

```bash
python -m venv env
```

### 4. Activar entorno virtual

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Configurar variables de entorno

Crear un archivo `.env`:

```env
SECRET_KEY=tu_clave
DB_NAME=cliente
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

### 7. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Ejecutar el servidor

```bash
python manage.py runserver
```

---

## 🌐 Acceso

Una vez iniciado el proyecto:

```text
http://127.0.0.1:8000/
```

---

## 📸 Capturas

Agrega aquí imágenes del proyecto:

```md
![Login](images/login.png)

![Dashboard](images/dashboard.png)

![Usuarios](images/users.png)
```

---

## 🎯 Objetivo del Proyecto

Este proyecto fue desarrollado con fines académicos para fortalecer conocimientos en:

- Desarrollo Web con Django
- Arquitectura MVC/MVT
- Gestión de usuarios y permisos
- Bases de datos relacionales
- Seguridad web
- Diseño de interfaces modernas

---

## 👨‍💻 Autor

**Anderson Clever**
Tecnólogo en Análisis y Desarrollo de Software

GitHub: https://github.com/TU-USUARIO

---

## 📄 Licencia

Este proyecto es de uso educativo y académico.
