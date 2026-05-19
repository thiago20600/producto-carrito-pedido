from datetime import datetime, timezone
from typing import Literal
from sqlmodel import Field, Relationship, SQLModel

from models.links import PedidoProductoLink

class Pedido(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    carrito_id: int = Field(foreign_key="carrito.id")
    carrito: "Carrito" = Relationship()
    estado: Literal['activo', 'en_proceso','entregado', 'cancelado'] = 'activo'
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default=None)
    canceled_at: datetime | None = Field(default=None)
    user_id: int = Field(foreign_key="user.id")
    comentarios: str | None = None
    productos: list["Producto"] = Relationship(back_populates="pedidos", link_model=PedidoProductoLink)


class PedidoPublic(SQLModel):
    id: int
    carrito_id: int
    estado: Literal['activo', 'en_proceso','entregado', 'cancelado']
    created_at: datetime
    updated_at: datetime | None
    canceled_at: datetime | None
    user_id: int
    comentarios: str | None