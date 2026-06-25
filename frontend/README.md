# Frontend - Usuarios Eventos App

Este README explica cómo usar y ejecutar la parte del frontend de la aplicación.
El frontend es una SPA simple hecha con **HTML, CSS y JavaScript** que consume la API del backend.

## 📌 Contenido

- Requisitos
- Cómo ejecutar el frontend
- Configurar la URL del backend
- Funcionalidades
- Estructura del frontend
- Notas importantes

---

## 🧩 Requisitos

Para ejecutar el frontend necesitas:

- Navegador moderno (Chrome, Edge, Firefox, Safari)
- Servir archivos estáticos desde `frontend/`
- Backend en funcionamiento y accesible desde `API_URL`

---

## 🚀 Ejecutar el Frontend

### Opción A: Live Server en VS Code

1. Abre la carpeta `frontend/` en VS Code.
2. Instala la extensión **Live Server** o **Five Server**.
3. Haz clic derecho en `index.html` y selecciona `Open with Live Server`.
4. El navegador abrirá la app en una URL como `http://127.0.0.1:5500`.

### Opción B: Python HTTP server

```bash
cd frontend
python -m http.server 5500
```

Luego abre en el navegador:

```text
http://127.0.0.1:5500
```

### Opción C: http-server con Node.js

```bash
npm install -g http-server
cd frontend
http-server -p 5500
```

---

## 🔧 Configurar la URL del Backend

El archivo principal es `frontend/js/app.js`.
Busca esta línea:

```js
const API_URL = "https://usuarios-eventos-app.onrender.com";
```

Cámbiala a la URL donde corre tu backend local, por ejemplo:

```js
const API_URL = "http://localhost:8000";
```

> Si el backend está en otra URL, actualiza `API_URL` antes de usar la app.

---

## 🧠 Funcionalidades del Frontend

- Crear usuario
- Consultar todos los usuarios
- Editar usuario
- Eliminar usuario
- Buscar usuarios por nombre o email

Cuando creas, editas o eliminas un usuario, el frontend vuelve a cargar la lista automáticamente.

---

## 📁 Estructura del Frontend

```
frontend/
├── index.html
├── css/
│   └── styles.css
└── js/
    └── app.js
```

- `index.html` — interfaz principal de la app
- `css/styles.css` — estilos visuales
- `js/app.js` — lógica para consumir la API y manejar la UI

---

## 🧪 Probar la aplicación

1. Asegúrate de que el backend esté corriendo en `http://localhost:8000`.
2. Sirve el frontend en `http://127.0.0.1:5500`.
3. Abre la página en tu navegador.
4. Prueba crear un usuario, ver la lista y usar el buscador.

---

## ⚠️ Problemas comunes

### El frontend no carga usuarios
- Verifica que el backend esté ejecutando en `http://localhost:8000`
- Revisa `API_URL` en `frontend/js/app.js`
- Si usas otra dirección en el backend, actualiza `API_URL`

### CORS bloquea las peticiones
Revisa que el backend permite el origen del frontend en `main.py`:

```python
allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"]
```

### El botón de editar no funciona
- Comprueba que la respuesta del backend incluya `id` en cada usuario
- Verifica que la tabla `usuarios` tenga los campos esperados

---

## 💡 Consejos

- Si quieres usar el frontend y backend juntos en local, lo más cómodo es:
  - Backend: `http://localhost:8000`
  - Frontend: `http://127.0.0.1:5500`
- Guarda los cambios de `API_URL` antes de recargar la página.

---

## 📌 Resumen rápido

1. Sirve `frontend/index.html` desde un servidor local.
2. Ajusta `API_URL` en `frontend/js/app.js` al backend.
3. Abre `http://127.0.0.1:5500`.
4. Usa la interfaz para crear, editar, listar y eliminar usuarios.

## ℹ️ IMPORTANTE
La url desplegada en este momento es:
https://hernan-dagata.github.io/usuarios-eventos-app/

