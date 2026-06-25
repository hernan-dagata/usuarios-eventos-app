# 🚀 Users API - FastAPI + Supabase + RabbitMQ

Microservicio de usuarios con arquitectura basada en eventos, construido con FastAPI, Supabase y RabbitMQ.

---

## 🧠 Arquitectura

Este servicio sigue un enfoque de Event-Driven Architecture:

FastAPI → Supabase → RabbitMQ → consumidores de eventos

Cada operación del CRUD genera un evento publicado en RabbitMQ.

---

## 📦 Funcionalidades

CRUD completo de usuarios:

- Crear usuario
- Consultar usuarios
- Actualizar usuario
- Eliminar usuario

---

## 📡 Eventos del sistema

Cada operación genera un evento con su respectivo tipo:

- user.events.app.created
- user.events.app.retrieved
- user.events.app.updated
- user.events.app.deleted

---

## 📌 Ejemplo de evento

```json
{
  "id": "uuid",
  "type": "user.events.app.created",
  "version": "1.0",
  "time_stamp": "2026-06-24T00:00:00-05:00",
  "source": "users-api",
  "correlation_id": "uuid",
  "data": {
    "id": 1,
    "name": "Juan",
    "email": "juan@test.com"
  }
}
```

---

## 🛠️ Tecnologías

- Python 3.10+
- FastAPI
- Supabase
- RabbitMQ
- Pika
- python-dotenv

---

## ⚙️ Configuración

Crear archivo `.env` en la raíz del proyecto:

```
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
```

---

## ▶️ Ejecución local

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el servidor:

```bash
uvicorn main:app --reload
```

La API quedará disponible en:

http://localhost:8000

---

## 📬 Endpoints

### Crear usuario
POST /usuarios

### Consultar usuarios
GET /usuarios

### Actualizar usuario
PUT /usuarios/{id}

### Eliminar usuario
DELETE /usuarios/{id}

---

## 🐇 RabbitMQ

### Configuración

- Exchange: domainEvents
- Tipo: topic
- Queue: usuarios.events.queue

### Routing keys

- user.events.app.created
- user.events.app.retrieved
- user.events.app.updated
- user.events.app.deleted

Cada evento se publica usando su routing key correspondiente.

---

## 📊 Flujo del sistema

Request → FastAPI → Supabase → Evento → RabbitMQ

---

## 🧪 Casos de uso

Este proyecto sirve para:

- Arquitectura basada en eventos
- Microservicios
- Pruebas automatizadas (QA / integración)
- Trazabilidad de datos
- Aprendizaje de mensajería con RabbitMQ

---

## 🚀 Próximos pasos

- Dockerizar el servicio
- Agregar tests automatizados
- Implementar patrón Outbox
- Deploy en nube (Render / Railway / AWS)
- Observabilidad de eventos

---

## 👨‍💻 Autor

Hernan Garcia
