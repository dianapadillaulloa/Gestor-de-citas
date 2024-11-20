from fastapi import FastAPI, HTTPException
import mysql.connector
from modulos.schema import FacturaCitas, FacturaExample
from conexion.conexion import conn
from cors.cors import app

app = FastAPI()

# CRUD para `facture_citas`

# Endpoint para crear una nueva factura de citas médicas
@app.post('/facturas/citas/')
async def create_factura_citas(factura: FacturaCitas):
    cursor = conn.cursor()
    query = """
        INSERT INTO facture_citas (id_citas_medicas, fecha, hora, costo, medio_pago, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        factura.id_citas_medicas,
        factura.fecha,
        factura.hora,
        factura.costo,
        factura.medio_pago,
        factura.estado
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'La factura de cita médica fue registrada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar la factura de cita médica: {err}") from err
    finally:
        cursor.close()

# Endpoint para listar todas las facturas de citas médicas
@app.get('/facturas/citas/')
async def get_facturas_citas():
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM facture_citas"
        cursor.execute(query)
        facturas = cursor.fetchall()
        return facturas
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener las facturas de citas médicas: {err}") from err
    finally:
        cursor.close()

# Endpoint para obtener una factura de citas médicas por ID
@app.get('/facturas/citas/{id_factura}')
async def get_factura_citas(id_factura: int):
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM facture_citas WHERE id_fac_citas = %s"
        cursor.execute(query, (id_factura,))
        factura = cursor.fetchone()
        if not factura:
            raise HTTPException(status_code=404, detail="Factura de cita médica no encontrada")
        return factura
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener la factura: {err}") from err
    finally:
        cursor.close()

# Endpoint para actualizar una factura de citas médicas por ID
@app.put('/facturas/citas/{id_factura}')
async def update_factura_citas(id_factura: int, factura: FacturaCitas):
    cursor = conn.cursor()
    query = """
        UPDATE facture_citas
        SET id_citas_medicas = %s, fecha = %s, hora = %s, costo = %s, medio_pago = %s, estado = %s
        WHERE id_fac_citas = %s
    """
    values = (
        factura.id_citas_medicas,
        factura.fecha,
        factura.hora,
        factura.costo,
        factura.medio_pago,
        factura.estado,
        id_factura
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'La factura de cita médica fue actualizada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la factura: {err}") from err
    finally:
        cursor.close()

# Endpoint para eliminar una factura de citas médicas por ID
@app.delete('/facturas/citas/{id_factura}')
async def delete_factura_citas(id_factura: int):
    cursor = conn.cursor()
    query = "DELETE FROM facture_citas WHERE id_fac_citas = %s"

    try:
        cursor.execute(query, (id_factura,))
        conn.commit()
        return {'message': 'La factura de cita médica fue eliminada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la factura: {err}") from err
    finally:
        cursor.close()


# CRUD para `facture_example`

# Endpoint para crear una nueva factura de example
@app.post('/facturas/example/')
async def create_factura_example(factura: FacturaExample):
    cursor = conn.cursor()
    query = """
        INSERT INTO facture_example (id_example, fecha, hora, costo, medio_pago, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        factura.id_example,
        factura.fecha,
        factura.hora,
        factura.costo,
        factura.medio_pago,
        factura.estado
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'La factura de ejemplo fue registrada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar la factura de ejemplo: {err}") from err
    finally:
        cursor.close()

# Endpoint para listar todas las facturas de example
@app.get('/facturas/example/')
async def get_facturas_example():
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM facture_example"
        cursor.execute(query)
        facturas = cursor.fetchall()
        return facturas
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener las facturas de ejemplo: {err}") from err
    finally:
        cursor.close()

# Endpoint para actualizar una factura de example por ID
@app.put('/facturas/example/{id_factura}')
async def update_factura_example(id_factura: int, factura: FacturaExample):
    cursor = conn.cursor()
    query = """
        UPDATE facture_example
        SET id_example = %s, fecha = %s, hora = %s, costo = %s, medio_pago = %s, estado = %s
        WHERE id_fact = %s
    """
    values = (
        factura.id_example,
        factura.fecha,
        factura.hora,
        factura.costo,
        factura.medio_pago,
        factura.estado,
        id_factura
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'La factura de ejemplo fue actualizada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la factura: {err}") from err
    finally:
        cursor.close()

# Endpoint para eliminar una factura de example por ID
@app.delete('/facturas/example/{id_factura}')
async def delete_factura_example(id_factura: int):
    cursor = conn.cursor()
    query = "DELETE FROM facture_example WHERE id_fact = %s"

    try:
        cursor.execute(query, (id_factura,))
        conn.commit()
        return {'message': 'La factura de ejemplo fue eliminada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la factura: {err}") from err
    finally:
        cursor.close()

conn.close()
