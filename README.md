# 👥 Usuarios-Eventos App

Una aplicación web completa para la gestión de usuarios con arquitectura de eventos y mensajería asincrónica. Combina un backend robusto en **FastAPI** con un frontend interactivo en **HTML/CSS/JavaScript**.

## 🎯 Descripción

Esta aplicación permite:
- ✅ **Crear** nuevos usuarios con nombre y email
- ✅ **Consultar** listado completo de usuarios
- ✅ **Editar** datos de usuarios existentes
- ✅ **Eliminar** usuarios del sistema
- ✅ **Buscar** usuarios en tiempo real
- ✅ **Registrar eventos** de todas las operaciones mediante RabbitMQ

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8+** → [Descargar Python](https://www.python.org/downloads/)
- **Git** → [Descargar Git](https://git-scm.com/)
- **Node.js y npm** (opcional, si deseas servir el frontend con un servidor) → [Descargar Node.js](https://nodejs.org/)
- **RabbitMQ** (para mensajería de eventos) → [Descargar RabbitMQ](https://www.rabbitmq.com/download.html)
- **Cuenta en Supabase** (base de datos en la nube) → [Crear cuenta en Supabase](https://supabase.com)

---

## 🚀 Guía de Instalación

### 1️⃣ Clona el Repositorio

```bash
git clone https://github.com/tu-usuario/usuarios-eventos-app.git
cd usuarios-eventos-app
```

---

### 2️⃣ Configuración del Backend

#### Instalación de Dependencias

```bash
# Navega a la carpeta del backend
cd backend

# Crea un entorno virtual (recomendado)
# En Windows:
python -m venv venv
venv\Scripts\activate

# En macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt
```

#### Configura las Variables de Entorno

Crea un archivo `.env` en la carpeta `backend/` con los siguientes valores:

```env
# Supabase
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu-clave-api-supabase

# RabbitMQ
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USER=guest
RABBITMQ_PASSWORD=guest

# FastAPI
ENVIRONMENT=development
DEBUG=True
```

**¿Cómo obtener las credenciales de Supabase?**
1. Entra a [Supabase](https://supabase.com)
2. Crea un nuevo proyecto
3. Ve a `Settings → API` para obtener tu URL y clave API
4. Asegúrate de crear una tabla `usuarios` con los campos: `id`, `name`, `email`, `created_at`

---

### 3️⃣ Instalación y Configuración de RabbitMQ

#### En Windows

```bash
# Descarga e instala RabbitMQ desde:
# https://www.rabbitmq.com/install-windows.html

# Luego inicia el servicio (se inicia automáticamente después de instalar)
# O manualmente:
"C:\Program Files\RabbitMQ Server\rabbitmq_server-3.x.x\sbin\rabbitmq-server.bat"
```

#### En macOS

```bash
# Con Homebrew
brew install rabbitmq

# Inicia RabbitMQ
brew services start rabbitmq

# O manualmente:
rabbitmq-server
```

#### En Linux (Ubuntu/Debian)

```bash
# Instala RabbitMQ
sudo apt-get install rabbitmq-server

# Inicia el servicio
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server

# Verifica el estado
sudo systemctl status rabbitmq-server
```

**Verificación:** Accede a `http://localhost:15672` con credenciales por defecto (`guest`/`guest`)
**Nota:** tambien puedes crear una instancia directamente en la nube a traves de https://customer.cloudamqp.com/instance


---

### 4️⃣ Configuración del Frontend

El frontend es una aplicación estática (HTML/CSS/JS vanilla), así que no necesita instalación de dependencias. Pero necesitas servir los archivos correctamente.

#### Opción A: Live Server (Recomendado en desarrollo)

Si usas **VS Code**:
1. Instala la extensión **Live Server** (Five Server)
2. Click derecho en `frontend/index.html` → **Open with Live Server**
3. El navegador se abrirá en `http://127.0.0.1:5500`

#### Opción B: Python HTTP Server

```bash
# Navega a la carpeta frontend
cd frontend

# Inicia un servidor HTTP simple
python -m http.server 8000

# Accede a http://localhost:8000
```

#### Opción C: Node.js (http-server)

```bash
# Instala http-server globalmente
npm install -g http-server

# Navega a frontend y sirve
cd frontend
http-server -p 8000

# Accede a http://localhost:8000
```

---

## 🏃 Levantar la Aplicación Localmente

### Paso 1: Inicia RabbitMQ

```bash
# Windows (si no está configurado como servicio)
"C:\Program Files\RabbitMQ Server\rabbitmq_server-3.x.x\sbin\rabbitmq-server.bat"

# macOS
brew services start rabbitmq

# Linux
sudo systemctl start rabbitmq-server
```

**Verifica que esté corriendo:** Abre `http://localhost:15672` en tu navegador

---

### Paso 2: Inicia el Backend

En una terminal nueva:

```bash
cd backend

# Activa el entorno virtual (si no está activado)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Inicia el servidor FastAPI
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Resultado esperado:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

**Prueba la API:** Abre `http://localhost:8000/docs` para ver la documentación interactiva de Swagger

---

### Paso 3: Inicia el Frontend

En otra terminal:

```bash
cd frontend

# Opción A: Live Server (VS Code - extension)
# Click derecho en index.html → Open with Live Server

# Opción B: Python
python -m http.server 5500

# Opción C: http-server
http-server -p 5500
```

**Resultado esperado:** El navegador abre `http://localhost:5500` (o `http://127.0.0.1:5500`)

---

## 📁 Estructura del Proyecto

```
usuarios-eventos-app/
├── backend/                          # 🔙 Backend FastAPI
│   ├── main.py                      # Archivo principal con endpoints
│   ├── models.py                    # Modelos Pydantic
│   ├── database.py                  # Conexión con Supabase
│   ├── requirements.txt             # Dependencias Python
│   ├── .env                         # Variables de entorno (no commitear)
│   ├── messaging/
│   │   ├── events.py               # Creación de eventos
│   │   └── rabbitmq.py             # Configuración de RabbitMQ
│   ├── utils/
│   │   └── time.py                 # Utilidades de tiempo
│   └── test_rabbit.py              # Tests para RabbitMQ
│
├── frontend/                         # 🎨 Frontend HTML/CSS/JS
│   ├── index.html                   # Página principal
│   ├── css/
│   │   └── styles.css              # Estilos
│   └── js/
│       └── app.js                  # Lógica de la aplicación
│
├── README.md                         # Este archivo
└── LICENSE                           # Licencia del proyecto
```

---

## 🔌 Endpoints de la API

### Base URL: `http://localhost:8000`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Verifica que la API esté funcionando |
| `GET` | `/usuarios` | Obtiene la lista de todos los usuarios |
| `POST` | `/usuarios` | Crea un nuevo usuario |
| `PUT` | `/usuarios/{user_id}` | Actualiza un usuario existente |
| `DELETE` | `/usuarios/{user_id}` | Elimina un usuario |
| `GET` | `/docs` | Documentación interactiva de Swagger |
| `GET` | `/redoc` | Documentación ReDoc alternativa |

### Ejemplos de Uso

#### Crear un Usuario
```bash
curl -X POST "http://localhost:8000/usuarios" \
  -H "Content-Type: application/json" \
  -d '{"name": "Juan Pérez", "email": "juan@example.com"}'
```

#### Obtener Todos los Usuarios
```bash
curl "http://localhost:8000/usuarios"
```

#### Actualizar un Usuario
```bash
curl -X PUT "http://localhost:8000/usuarios/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Juan Carlos", "email": "juan.carlos@example.com"}'
```

#### Eliminar un Usuario
```bash
curl -X DELETE "http://localhost:8000/usuarios/1"
```

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **FastAPI** - Framework web moderno y rápido
- **Uvicorn** - Servidor ASGI
- **Pydantic** - Validación de datos
- **Supabase** - Base de datos PostgreSQL en la nube
- **Pika** - Cliente Python para RabbitMQ
- **Python-dotenv** - Gestión de variables de entorno

### Frontend
- **HTML5** - Estructura
- **CSS3** - Estilos y diseño responsivo
- **JavaScript (Vanilla)** - Lógica interactiva
- **Fetch API** - Comunicación con el backend

### Herramientas Adicionales
- **RabbitMQ** - Cola de mensajes para eventos asincrónico
- **Git** - Control de versiones
- **Docker** (opcional) - Para containerización

---

## 📊 Arquitectura de Eventos

La aplicación utiliza **RabbitMQ** para publicar eventos cuando ocurren cambios:

- 📤 **user.events.app.created** - Se dispara cuando se crea un usuario
- 📤 **user.events.app.updated** - Se dispara cuando se actualiza un usuario
- 📤 **user.events.app.deleted** - Se dispara cuando se elimina un usuario
- 📤 **user.events.app.retrieved** - Se dispara cuando se consulta la lista de usuarios

---

## 🐛 Solución de Problemas

### ❌ Error: "No module named 'fastapi'"
```bash
# Asegúrate de estar en el entorno virtual y luego:
pip install -r requirements.txt
```

### ❌ Error: "Connection refused" al conectar a RabbitMQ
```bash
# Verifica que RabbitMQ esté ejecutándose:
# Windows - Abre Task Manager y busca "RabbitMQ"
# macOS/Linux - Ejecuta:
# brew services list  (macOS)
# systemctl status rabbitmq-server  (Linux)

# Si no está corriendo, inícialo:
brew services start rabbitmq  # macOS
sudo systemctl start rabbitmq-server  # Linux
```

### ❌ Error: "CORS policy" en el frontend
Asegúrate que en `backend/main.py` el `allow_origins` incluye tu URL local:
```python
allow_origins=["http://127.0.0.1:5500", "http://localhost:5500", ...]
```

### ❌ Error: "Tabla 'usuarios' no existe"
1. Ve a tu proyecto en Supabase
2. Crea una nueva tabla llamada `usuarios`
3. Añade columnas: `id` (bigint, primary key), `name` (text), `email` (text), `created_at` (timestamp)

### ❌ El frontend no se conecta al backend
Verifica:
1. El backend está corriendo en `http://localhost:8000`
2. En `frontend/js/app.js`, la variable `API_URL` apunta a la URL correcta
3. El backend tiene CORS configurado correctamente

---

## 📦 Variables de Entorno (.env)

Crea un archivo `.env` en la carpeta `backend/` (NO lo commits a Git):

```env
# ========== SUPABASE ==========
SUPABASE_URL=https://tu-id-proyecto.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# ========== RABBITMQ ==========
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USER=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_VHOST=/

# ========== FASTAPI ==========
ENVIRONMENT=development
DEBUG=True
LOG_LEVEL=info
```

---

## 🚢 Deploy (Producción)

### Opción 1: Render (Backend)

1. Sube el proyecto a GitHub
2. Ve a [Render.com](https://render.com)
3. Crea un nuevo "Web Service"
4. Conecta tu repositorio GitHub
5. Configura las variables de entorno
6. Deploy 🚀

### Opción 2: Vercel (Frontend)

1. Ve a [Vercel.com](https://vercel.com)
2. Importa tu repositorio GitHub
3. Vercel detecta automáticamente el frontend
4. Deploy 🚀

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

---

