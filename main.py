from contextlib import asynccontextmanager

from fastapi import FastAPI
from database.engine import create_db_and_tables
from router.producto import router as productoRouter
from models.categorias import Categoria
from models.productos import Producto


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(productoRouter)