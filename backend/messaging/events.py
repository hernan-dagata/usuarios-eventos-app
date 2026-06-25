from datetime import datetime, timezone
from uuid import uuid4
from utils.time import now_colombia

def crear_evento_usuarios_consultados(usuarios):
    return {
        "id": str(uuid4()),
        "type": "user.events.app.retrieved",
        "version": "1.0",
        "time_stamp": now_colombia(),
        "source": "users-api",
        "correlation_id": str(uuid4()),
        "data": {
            "count": len(usuarios),
            "users": usuarios,
            "retrieved_at": now_colombia()
        }
    }
    
def crear_evento_usuario_creado(usuario):
    return {
        "id": str(uuid4()),
        "type": "user.events.app.created",
        "version": "1.0",
        "timestamp": now_colombia(),
        "source": "users-api",
        "correlation_id": str(uuid4()),
        "data": {
            "id": usuario["id"],
            "name": usuario["name"],
            "email": usuario["email"],
            "created_at": usuario["created_at"]
        }
    }

def crear_evento_usuario_actualizado(usuario_anterior, usuario_nuevo):
    return {
        "id": str(uuid4()),
        "type": "user.events.app.updated",
        "version": "1.0",
        "time_stamp": now_colombia(),
        "source": "users-api",
        "correlation_id": str(uuid4()),
        "data": {
            "id": usuario_nuevo["id"],
            "before": {
                "name": usuario_anterior.get("name"),
                "email": usuario_anterior.get("email")
            },
            "after": {
                "name": usuario_nuevo.get("name"),
                "email": usuario_nuevo.get("email")
            },
            "updated_at": now_colombia()
        }
    }
    
def crear_evento_usuario_eliminado(usuario):
    return {
        "id": str(uuid4()),
        "type": "user.events.app.deleted",
        "version": "1.0",
        "time_stamp": now_colombia(),
        "source": "users-api",
        "correlation_id": str(uuid4()),
        "data": {
            "id": usuario["id"],
            "name": usuario.get("name"),
            "email": usuario.get("email"),
            "deleted_at": now_colombia()
        }
    }