from sqlmodel import Field, Relationship,SQLModel
from models.categorias import CategoriaPublic
from models.links import PedidoProductoLink, ProductosCategoriaLink
from datetime import date, datetime, timezone

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    categoria: list['Categoria'] = Relationship(back_populates='producto', link_model=ProductosCategoriaLink)
    sku: int | None = Field(default=None, index=True)
    precio: float = Field(gt=0, index=True)
    stock: int = Field(ge=0, index=True)
    descripcion: str | None = Field(default=None, max_length=1200)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default=None)
    user_email: str
    pedidos: list["Pedido"] = Relationship(back_populates="productos", link_model=PedidoProductoLink)


class ProductoPublic(SQLModel):
    nombre: str
    categorias: list[CategoriaPublic]
    precio: float
    stock: int
    descripcion: str | None


class ProductCreate(SQLModel):
    nombre: str
    categoria: str
    sku: int | None
    precio: float
    stock: int
    descripcion: str | None
    user_email: str


class ProductUpdate(SQLModel):
    nombre: str | None = None
    categoria: str | None = None
    sku: int | None = None
    precio: float | None = None
    stock: int | None = None
    descripcion: str | None = None