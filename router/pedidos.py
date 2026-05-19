from fastapi import APIRouter, Depends
from sqlmodel import select
from models.pedido import Pedido, PedidoPublic
from database.engine import SessionDep
from utils.auth import require_admin


router = APIRouter()


@router.get('/pedidos/', response_model=PedidoPublic, dependencies=[Depends(require_admin)])
async def get_pedidos(session: SessionDep):
    pedidos = session.exec(select(Pedido))
    return pedidos