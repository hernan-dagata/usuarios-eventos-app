# Backend - Usuarios Eventos App

Este README describe cómo configurar y ejecutar la parte del backend de la aplicación.
El backend está construido con **FastAPI**, usa **Supabase** como base de datos y publica eventos en **RabbitMQ**.

## 📌 Contenido

- Requisitos
- Instalación
- Configuración de variables de entorno
- Ejecutar la API
- Endpoints disponibles
- Eventos de RabbitMQ
- Probar la conexión a RabbitMQ
- Notas adicionales

---

## 🧩 Requisitos

Antes de ejecutar el backend necesitas:

- Python 3.8+ instalado
- RabbitMQ en ejecución
- Cuenta y proyecto en Supabase
- Las credenciales de Supabase

---

## ⚙️ Instalación

1. Abre una terminal en la carpeta `backend/`.
2. Crea el entorno virtual:

```bash
python -m venv venv
```

3. Activa el entorno virtual:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Variables de Entorno

El backend lee la configuración desde un archivo `.env` usando `python-dotenv`.
Crea un archivo `.env` en `backend/` con estas variables:

```env
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu-clave-secreta-supabase
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
```

### Detalles importantes

- `SUPABASE_URL`: URL de tu proyecto Supabase.
- `SUPABASE_KEY`: clave API de Supabase.
- `RABBITMQ_URL`: URL de conexión a RabbitMQ.
  - Ejemplo local: `amqp://guest:guest@localhost:5672/`
  - Ajusta usuario, contraseña, host, puerto y vhost según tu instalación.

---

## 🚀 Ejecutar la API

Con el entorno virtual activado y el archivo `.env` configurado:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La API quedará disponible en:

- http://localhost:8000
- Documentación automática: http://localhost:8000/docs

---

## 📡 Endpoints del Backend

| Método | Ruta | Descripción |
| ------ | ---- | ----------- |
| `GET` | `/` | Verifica que el backend funcione |
| `GET` | `/usuarios` | Lista todos los usuarios |
| `POST` | `/usuarios` | Crea un usuario nuevo |
| `PUT` | `/usuarios/{user_id}` | Actualiza un usuario existente |
| `DELETE` | `/usuarios/{user_id}` | Elimina un usuario |

### Ejemplo de solicitud POST

```bash
curl -X POST "http://localhost:8000/usuarios" \
  -H "Content-Type: application/json" \
  -d '{"name": "Ana", "email": "ana@example.com"}'
```

---

## 🐇 Eventos RabbitMQ

El backend publica eventos de dominio cada vez que se realizan operaciones sobre usuarios.
Los eventos se envían al exchange `domainEvents` con routing keys específicas.

### Routing keys usados

- `user.events.app.created`
- `user.events.app.updated`
- `user.events.app.deleted`
- `user.events.app.retrieved`

### Archivos relevantes

- `messaging/rabbitmq.py` — configura la conexión y publica los mensajes
- `messaging/events.py` — crea la estructura de los eventos JSON

---

## 🧪 Probar RabbitMQ

Puedes validar la conexión publicando un mensaje de prueba con `test_rabbit.py`.

```bash
python test_rabbit.py
```

Si la publicación es exitosa, deberías ver el mensaje:

```text
Evento enviado correctamente
```

---

## 🗄️ Configuración de Supabase

El backend espera una tabla llamada `usuarios` con al menos las columnas:

- `id`
- `name`
- `email`
- `created_at`

Asegúrate de que tu tabla exista y tenga estos campos antes de ejecutar la API.

---

## 💡 Notas adicionales

- La ruta CORS en `main.py` ya permite solicitudes desde:
  - `http://127.0.0.1:5500`
  - `http://localhost:5500`
- Si sirves el frontend en otra dirección, añade esa URL a `allow_origins`.
- El backend carga `dotenv` desde `database.py` y `rabbitmq.py`, así que el archivo `.env` debe estar en la carpeta `backend/`.

---

## 📁 Estructura del backend

```
backend/
├── main.py
├── models.py
├── database.py
├── requirements.txt
├── .env
├── test_rabbit.py
└── messaging/
    ├── events.py
    └── rabbitmq.py
```

---

## ✅ Resumen rápido

1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\activate` o `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Crear `.env` con Supabase y RabbitMQ
6. `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

¡El backend estará listo para recibir peticiones y publicar eventos en RabbitMQ!

## ℹ️ IMPORTANTE
La url desplegada en este momento es:
https://usuarios-eventos-app.onrender.com