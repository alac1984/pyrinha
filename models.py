from datetime import date
from uuid import UUID

from sqlmodel import SQLModel, Field


class PessoaCreate(SQLModel)
    apelido: str = Field(unique=True)
    nome: str
    nascimento: date
    stack: list[str] | None


class Pessoa(PessoaCreate, table=True):
    id: UUID = Field(primary_key=True)
