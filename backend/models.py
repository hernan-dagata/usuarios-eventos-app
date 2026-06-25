from pydantic import BaseModel

class Usuario(BaseModel):
    name: str
    email: str