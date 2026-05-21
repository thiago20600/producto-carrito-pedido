from datetime import datetime, timezone
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel
from models.links import PedidoProductoLink



class EstadoPedido(str, Enum):
    activo = 'activo'
    en_proceso = 'en_proceso'
    entregado = 'entregado'
    cancelado = 'cancelado'


class Pedido(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    carrito_id: int = Field(foreign_key="carrito.id")
    carrito: 'Carrito' = Relationship(back_populates='pedido')
    estado: EstadoPedido = Field(default=EstadoPedido.activo)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default=None)
    canceled_at: datetime | None = Field(default=None)
    entregado_at: datetime | None = Field(default=None)
    user_email: str
    comentarios: str | None = None
    productos: list['Producto'] = Relationship(back_populates="pedidos", link_model=PedidoProductoLink)


class PedidoPublic(SQLModel):
    id: int
    carrito_id: int
    estado: EstadoPedido
    created_at: datetime
    updated_at: datetime | None
    canceled_at: datetime | None
    user_email: str
    comentarios: str | None


class PedidoUpdate(SQLModel):
    estado: EstadoPedido | None = None
    comentarios: str | None = None