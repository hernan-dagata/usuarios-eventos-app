from fastapi import FastAPI
from database import supabase
from models import Usuario
from messaging.events import (
    crear_evento_usuarios_consultados,
    crear_evento_usuario_creado,
    crear_evento_usuario_actualizado,
    crear_evento_usuario_eliminado,
)
from messaging.rabbitmq import configurar_rabbit, publicar_evento
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Usuarios API", description="API con Supabase y RabbitMQ")


@app.options("/{path:path}")
def options_handler(path: str):
    return {"message": "OPTIONS OK"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    configurar_rabbit()


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}


@app.get("/usuarios")
def obtener_usuarios():
    respuesta = supabase.table("usuarios").select("*").execute()
    usuarios = respuesta.data
    evento = crear_evento_usuarios_consultados(usuarios)
    publicar_evento(evento, "user.events.app.retrieved")
    return usuarios


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    nuevo_usuario = (
        supabase.table("usuarios")
        .insert({"name": usuario.name, "email": usuario.email})
        .execute()
    )
    usuario_creado = nuevo_usuario.data[0]
    evento = crear_evento_usuario_creado(usuario_creado)
    publicar_evento(evento, "user.events.app.created")
    return usuario_creado


@app.put("/usuarios/{user_id}")
def actualizar_usuario(user_id: int, usuario: Usuario):
    existente = supabase.table("usuarios").select("*").eq("id", user_id).execute()
    if not existente.data:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_anterior = existente.data[0]
    actualizado = (
        supabase.table("usuarios")
        .update({"name": usuario.name, "email": usuario.email})
        .eq("id", user_id)
        .execute()
    )
    usuario_nuevo = actualizado.data[0]
    evento = crear_evento_usuario_actualizado(usuario_anterior, usuario_nuevo)
    publicar_evento(evento, "user.events.app.updated")
    return usuario_nuevo


@app.delete("/usuarios/{user_id}")
def eliminar_usuario(user_id: int):
    existente = supabase.table("usuarios").select("*").eq("id", user_id).execute()
    if not existente.data:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario = existente.data[0]
    supabase.table("usuarios").delete().eq("id", user_id).execute()
    evento = crear_evento_usuario_eliminado(usuario)
    publicar_evento(evento, "user.events.app.deleted")
    return {"mensaje": "Usuario eliminado", "id": user_id}
