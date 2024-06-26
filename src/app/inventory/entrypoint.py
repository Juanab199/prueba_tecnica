import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.inventory.schemas.entry_data_schemas import ProductSch, OrderSch, StockUpdate
from app.inventory.schemas.output_schemas import ResponseSch
from app.db.config import get_db, Base, engine
from app.db.db_controller import DbController
from app.common.execptions import NotFoundProduct, InsufficientProducts
from fastapi import HTTPException


Base.metadata.create_all(bind=engine)
db_controller = DbController()

task_router = APIRouter(prefix="/api")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@task_router.post(
    path="/products",
    status_code=201
)
async def create_product(product: ProductSch, db: Session = Depends(get_db)):
    db_controller.db_session = db
    db_controller.create_product(product=product)
    logging.info("Se ha creado un producto")
    return ResponseSch(
        status="Ok",
        msg="Se ha creado correctamente el producto"
    )

@task_router.patch(
    path="/inventories/product/{product_id}",
    status_code=200
)
async def add_stock(product_id: str, stocksch: StockUpdate, db: Session = Depends(get_db)):
    try: 
        db_controller.db_session = db
        db_controller.update_product_stock(product_id=product_id, num_stock_to_add=stocksch.stock)
        logging.info("Se ha actualizado el stock de un producto")
        return ResponseSch(
            status="Ok",
            code=200,
            msg="Se actualizo el stock del producto correctamente"
        )
    except NotFoundProduct:
        raise HTTPException(status_code=404, detail="Product no encontrado para actualizar")
    
@task_router.post(
    path="/orders",
    status_code=201
)
async def create_order(order: OrderSch, db: Session = Depends(get_db)):
    try:
        db_controller.db_session = db
        db_controller.create_order(order=order)
        logging.info("Se ha generado la venta")
        return ResponseSch(
            status="Ok",
            msg="Se registro la venta correctamente"
        )
    
    except NotFoundProduct:
        raise HTTPException(status_code=404, detail="Producto no encontrado no se puede vender")
    
    except InsufficientProducts:
        raise HTTPException(status_code=409, detail="Productos insuficientes")