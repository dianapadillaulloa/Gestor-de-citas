from fastapi import FastAPI, HTTPException
import mysql.connector
from modulos.schema import Doctor
from conexion.conexion import conn
from cors.cors import app

app = FastAPI()

# Endpoint para crear un nuevo doctor
@app.post('/doctores/')
async def create_doctor(doctor: Doctor):
    cursor = conn.cursor()
    query = """
        INSERT INTO doctores (nombre, apellido, identificacion, cuidad, telefono, gmail, sexo, edad, titulo, foto)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        doctor.nombre,
        doctor.apellido,
        doctor.identificacion,
        doctor.cuidad,
        doctor.telefono,
        doctor.gmail,
        doctor.sexo,
        doctor.edad,
        doctor.titulo,
        doctor.foto
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'El doctor fue registrado correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar el doctor: {err}") from err
    finally:
        cursor.close()

# Endpoint para listar todos los doctores
@app.get('/doctores/')
async def get_doctores():
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM doctores"
        cursor.execute(query)
        doctores = cursor.fetchall()
        return doctores
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener los doctores: {err}") from err
    finally:
        cursor.close()

# Endpoint para obtener un doctor por ID
@app.get('/doctores/{id_doctor}')
async def get_doctor(id_doctor: int):
    cursor = conn.cursor(dictionary=True)

    try:
        query = "SELECT * FROM doctores WHERE id_doctor = %s"
        cursor.execute(query, (id_doctor,))
        doctor = cursor.fetchone()
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")
        return doctor
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener el doctor: {err}") from err
    finally:
        cursor.close()

# Endpoint para actualizar un doctor por ID
@app.put('/doctores/{id_doctor}')
async def update_doctor(id_doctor: int, doctor: Doctor):
    cursor = conn.cursor()
    query = """
        UPDATE doctores
        SET nombre = %s, apellido = %s, identificacion = %s, cuidad = %s, telefono = %s, gmail = %s, sexo = %s, edad = %s, titulo = %s, foto = %s
        WHERE id_doctor = %s
    """
    values = (
        doctor.nombre,
        doctor.apellido,
        doctor.identificacion,
        doctor.cuidad,
        doctor.telefono,
        doctor.gmail,
        doctor.sexo,
        doctor.edad,
        doctor.titulo,
        doctor.foto,
        id_doctor
    )

    try:
        cursor.execute(query, values)
        conn.commit()
        return {'message': 'El doctor fue actualizado correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el doctor: {err}") from err
    finally:
        cursor.close()

# Endpoint para eliminar un doctor por ID
@app.delete('/doctores/{id_doctor}')
async def delete_doctor(id_doctor: int):
    cursor = conn.cursor()
    query = "DELETE FROM doctores WHERE id_doctor = %s"

    try:
        cursor.execute(query, (id_doctor,))
        conn.commit()
        return {'message': 'El doctor fue eliminado correctamente'}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el doctor: {err}") from err
    finally:
        cursor.close()

conn.close()
