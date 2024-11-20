from fastapi import FastAPI, HTTPException
import mysql.connector
from modulos.schema import CitaMedica
from conexion.conexion import conn
from cors.cors import app

app = FastAPI()

# Endpoint para crear una nueva cita médica
@app.post('/citas/')
async def create_cita(cita: CitaMedica):
    cursor = conn.cursor()
    query = """
        INSERT INTO citas_medicas 
        (paciente, acompañante, fecha, hora, doctor, sexo, descripcion, costo_cita, id_paciente_acom)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        cita.paciente,
        cita.acompañante,
        cita.fecha,
        cita.hora,
        cita.doctor,
        cita.sexo,
        cita.descripcion,
        cita.costo_cita,
        cita.id_paciente_acom
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'La cita médica fue registrada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar la cita médica: {err}") from err
    finally:
        cursor.close()

# Endpoint para listar todas las citas médicas
@app.get('/citas/')
async def get_citas():
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
            SELECT id_citas, paciente, acompañante, fecha, hora, doctor, sexo, descripcion, costo_cita
            FROM citas_medicas
        """
        cursor.execute(query)
        citas = cursor.fetchall()
        return citas
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener las citas médicas: {err}") from err
    finally:
        cursor.close()

# Endpoint para obtener una cita médica por ID
@app.get('/citas/{id_cita}')
async def get_cita(id_cita: int):
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
            SELECT id_citas, paciente, acompañante, fecha, hora, doctor, sexo, descripcion, costo_cita
            FROM citas_medicas
            WHERE id_citas = %s
        """
        cursor.execute(query, (id_cita,))
        cita = cursor.fetchone()
        if not cita:
            raise HTTPException(status_code=404, detail="Cita médica no encontrada")
        return cita
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener la cita médica: {err}") from err
    finally:
        cursor.close()

# Endpoint para actualizar una cita médica por ID
@app.put('/citas/{id_cita}')
async def update_cita(id_cita: int, cita: CitaMedica):
    cursor = conn.cursor()
    query = """
        UPDATE citas_medicas
        SET paciente = %s, acompañante = %s, fecha = %s, hora = %s, doctor = %s, 
            sexo = %s, descripcion = %s, costo_cita = %s, id_paciente_acom = %s
        WHERE id_citas = %s
    """
    values = (
        cita.paciente,
        cita.acompañante,
        cita.fecha,
        cita.hora,
        cita.doctor,
        cita.sexo,
        cita.descripcion,
        cita.costo_cita,
        cita.id_paciente_acom,
        id_cita
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'La cita médica fue actualizada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la cita médica: {err}") from err
    finally:
        cursor.close()

# Endpoint para eliminar una cita médica por ID
@app.delete('/citas/{id_cita}')
async def delete_cita(id_cita: int):
    cursor = conn.cursor()
    query = "DELETE FROM citas_medicas WHERE id_citas = %s"

    try:
        cursor.execute(query, (id_cita,))
        conn.commit()
        return {'message': 'La cita médica fue eliminada correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la cita médica: {err}") from err
    finally:
        cursor.close()

conn.close()
