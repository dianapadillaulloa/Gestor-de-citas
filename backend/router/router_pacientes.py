from fastapi import FastAPI, HTTPException
import mysql.connector
from modulos.schema import Paciente
from conexion.conexion import conn
from cors.cors import app

app = FastAPI()

# Endpoint para crear un nuevo paciente
@app.post('/pacientes/')
async def create_paciente(paciente: Paciente):
    cursor = conn.cursor()
    query = """
        INSERT INTO pacientes (nombre, apellido, telefono, direccion, ciudad, acompañante)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        paciente.nombre,
        paciente.apellido,
        paciente.telefono,
        paciente.direccion,
        paciente.ciudad,
        paciente.acompañante
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'El paciente fue registrado correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar el paciente: {err}") from err
    finally:
        cursor.close()

# Endpoint para listar todos los pacientes
@app.get('/pacientes/')
async def get_pacientes():
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM pacientes"
        cursor.execute(query)
        pacientes = cursor.fetchall()
        return pacientes
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener los pacientes: {err}") from err
    finally:
        cursor.close()

# Endpoint para obtener un paciente por ID
@app.get('/pacientes/{id_pacientes}')
async def get_paciente(id_pacientes: int):
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM pacientes WHERE id_pacientes = %s"
        cursor.execute(query, (id_pacientes,))
        paciente = cursor.fetchone()
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return paciente
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener el paciente: {err}") from err
    finally:
        cursor.close()

# Endpoint para actualizar un paciente por ID
@app.put('/pacientes/{id_pacientes}')
async def update_paciente(id_pacientes: int, paciente: Paciente):
    cursor = conn.cursor()
    query = """
        UPDATE pacientes
        SET nombre = %s, apellido = %s, telefono = %s, direccion = %s, ciudad = %s, acompañante = %s
        WHERE id_pacientes = %s
    """
    values = (
        paciente.nombre,
        paciente.apellido,
        paciente.telefono,
        paciente.direccion,
        paciente.ciudad,
        paciente.acompañante,
        id_pacientes
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'El paciente fue actualizado correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el paciente: {err}") from err
    finally:
        cursor.close()

# Endpoint para eliminar un paciente por ID
@app.delete('/pacientes/{id_pacientes}')
async def delete_paciente(id_pacientes: int):
    cursor = conn.cursor()
    query = "DELETE FROM pacientes WHERE id_pacientes = %s"

    try:
        cursor.execute(query, (id_pacientes,))
        conn.commit()
        return {'message': 'El paciente fue eliminado correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el paciente: {err}") from err
    finally:
        cursor.close()

conn.close()
