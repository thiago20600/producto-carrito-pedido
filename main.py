from contextlib import asynccontextmanager

from fastapi import FastAPI
from database.engine import create_db_and_tables
from router.producto import router as productoRouter
from router.categoria import router as categoriaRouter
from router.pedidos import router as pedidoRouter
from models.categorias import Categoria
from models.productos import Producto


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(productoRouter)
app.include_router(pedidoRouter)
app.include_router(categoriaRouter)