from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from database.engine import SessionDep
from models.productos import ProductCreate, ProductUpdate, Producto, ProductoPublic
from utils.auth import get_current_user, require_admin
router = APIRouter()


@router.get('/productos', response_model=list[ProductoPublic])
async def get_all_products(session: SessionDep):
    products = session.exec(select(Producto)).all()
    return products


@router.get('/productos/{product_id}', response_model=ProductoPublic)
async def get_product(session: SessionDep, product_id: int):
    product = session.get(Producto, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


@router.post('/productos', response_model=ProductoPublic)
async def post_product(session: SessionDep,product: ProductCreate, current_user = Depends(require_admin)):
    db_product = Producto.model_validate(product)
    db_product.user_email = current_user['email']
    session.add(db_product)
    session.flush()

    return db_product


@router.patch('/productos/{product_id}', response_model=ProductoPublic, dependencies=[Depends(require_admin)])
async def patch_product(session: SessionDep, product_id: int, product: ProductUpdate):
    product_db = session.get(Producto, product_id)
    
    if not product_db:
        raise HTTPException(status_code=404, detail='Producto no encontrado')
    
    
    product_data = product.model_dump(exclude_unset=True)
    for key, value in product_data.items():
        setattr(product_db, key, value)
    
    product_db.updated_at = datetime.now(timezone.utc)

    session.add(product_db)
    session.refresh(product_db)
   
    return product_db


@router.delete('/productos/{product_id}', dependencies=[Depends(require_admin)])
async def delete_product(session: SessionDep, product_id: int):

    product_db = session.get(Producto, product_id)

    if not product_db:
        raise HTTPException(status_code=404, detail= 'Producto no encontrado')
    

    session.delete(product_db)

    return {'message': 'Producto eliminado'}
