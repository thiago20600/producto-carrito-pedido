from sqlmodel import Field, SQLModel
#sirve como tabla intermedia

class ProductosCategoriaLink(SQLModel, table=True):
    ProductoId: int | None = Field(default=None, foreign_key='producto.id', primary_key=True)
    CategoriaId: int | None = Field(default=None, foreign_key='categoria.id', primary_key=True)


class PedidoProductoLink(SQLModel, table=True):
    pedido_id: int = Field(foreign_key="pedido.id", primary_key=True)
    producto_id: int = Field(foreign_key="producto.id", primary_key=True)

    cantidad: int = Field(default=1)

    precio_unitario: float