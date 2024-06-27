# Prueba tecnica
## Microservicio para ejemplificar el control de inventario

Este servicio se contruyo en FasAPI, se selecciono este Framework porque es rápido y fácil de entender. Nos permite construir rápidamente APIs robustas con Python, aprovechando al máximo la velocidad del lenguaje.
Se utiliza pydantic para definir los esquemas de nuestros productos y órdenes, para asegurarnos que recibimos la información correcta.
Se utiliza SQLAlchemy ORM para gestionar los modelos e interacciones con la base de datos, ya que facilita la gestión de la base de datos sin complicaciones.
La base de datos es un Postgresql en la nube para la ejecución local o por el Dockerfile, para la ejecución con docker-compose se monta un servicio Postgresql en un contenedor que es accesible para el servicio de FastApi.

### Software requerido

- Python >= 3.9.4
- Docker

### Configuración de entorno de desarrollo

Es recomendable que se utilice un entorno virtual (_virtual environment_) de Python para el desarrollo y ejecución del microservicio en un entorno local.

Para la ejecución de los siguientes comandos se asume el uso de Windows y de PowerShell. 

#### Python virtual environment

```PowerShell
PS C:\...\prueba_tecnica> python -m venv <nombre de entorno virtual>
```

> Es convención usar `.venv` para nombrar todos los entornos virtuales que inicialicemos.

Se activa el entorno virtual y se agregan los modulos requeridos.

```PowerShell
PS C:\...\prueba_tecnica> .\.venv\Scripts\activate
(venv) PS C:\...\prueba_tecnica> pip install --upgrade pip
(venv) PS C:\...\prueba_tecnica> pip install -r requirements.txt
```


### Ejecución sin Docker

#### Ejecución de FastAPI app

```PowerShell
(venv) PS C:\...\prueba_tecnica> cd src
(venv) PS C:\...\prueba_tecnica\src> uvicorn app.main:app
```

### Ejecución con Docker

En caso de tener problemas para conectar a la base de datos

```PowerShell
(venv) PS C:\...\prueba_tecnica> docker-compose up --build -d
```

## Ruta del servicio
- **Sin docker**: `http://127.0.0.1:8000/api/`

- **En docker**: `http://localhost:8080/api/`

## Guía para usar el servicio

## Endpoints

### Ruta del swagger:
- **Swagger**: `/docs`

### 1. Crear Producto
- **Endpoint**: `/products`
- **Método HTTP**: `POST`
- **Descripción**: Crea un nuevo producto en el inventario.
- **Esquema de Entrada**:
  ```json
    {
      "sku": "string",
      "name": "string",
      "price": "number",
      "stock": "integer" (opcional, default 100)
    }
  ```

- **Ejemplo de Entrada**:
  ```json
    {
      "sku": "1001A",
      "name": "Producto Ejemplo",
      "price": 29.99,
      "stock": 150
    }
   ```
- **Respuesta del servicio**:
    ```json
      {
        "status": "Ok",
        "msg": "Se ha creado correctamente el producto"
      }
    ```

### 2.  Actualizar Stock de Producto
- **Endpoint**: ` /inventories/product/{product_id}`
- **Método HTTP**: `PATCH`
- **Descripción**: Actualiza el stock de un producto existente en el inventario.
- **Esquema de Entrada**:
  ```json
   {
     "stock": "integer"
   }
  ```

- **Ejemplo de Entrada**:
  ```json
    {
      "stock": 50
    }
   ```
- **Respuesta del servicio**:
    ```json
      {
        "status": "Ok",
        "msg": "Se actualizó el stock del product correctamente"
      }
    ```

### 3.  Crear Venta
- **Endpoint**: `/orders`
- **Método HTTP**: `POST`
- **Descripción**: Crea una nueva orden de venta.
- **Esquema de Entrada**:
  ```json
   {
      "order_id": "string",
      "products": [
        {
          "sku": "string",
          "quantity": "integer"
        }
      ]
    }
  ```

- **Ejemplo de Entrada**:
  ```json
    {
      "order_id": "ORD001",
      "products": [
        {
          "sku": "1001A",
          "quantity": 10
        },
        {
          "sku": "1002B",
          "quantity": 5
        }
      ]
    }
   ```
- **Respuesta del servicio**:
    ```json
      {
        "status": "Ok",
        "msg": "Se registró la venta correctamente"
      }
    ```

## Ejecucion de los tests unitarios
```PowerShell
(venv) PS C:\...\prueba_tecnica> pytest
```





