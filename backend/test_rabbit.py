from messaging.rabbitmq import publicar_evento


evento = {
    "event": "TEST_CONNECTION",
    "message": "Hola desde FastAPI"
}


publicar_evento(evento)

print("Evento enviado correctamente")