from datetime import datetime, timezone
from sqlmodel import Field, Relationship, SQLModel
from enum import Enum


class EstadoCarrito(Enum):
    abierto = 'abierto'
    confirmado = 'confirmado'
    cancelado = 'cancelado'


class Carrito(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_email: str
    estado: EstadoCarrito = Field(default=EstadoCarrito.abierto)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default=None)
    items: list['CarritoItem'] = Relationship(back_populates='carrito')
    pedido: 'Pedido' = Relationship(back_populates='carrito')


class CarritoItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    carrito_id: int = Field(foreign_key='carrito.id')
    carrito: 'Carrito' = Relationship(back_populates='items')
    producto_id: int = Field(foreign_key='producto.id')
    producto: 'Producto' = Relationship(back_populates='productos')
    cantidad: int = Field(default=1)
    precio_unitario: float = Field(gt=0)