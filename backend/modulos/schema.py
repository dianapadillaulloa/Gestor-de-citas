from pydantic import BaseModel # Importa módulos de terceros primero
import mysql.connector 
from conexion.conexion import conn

# Modelo para la tabla "pacientes"
class Paciente(BaseModel):
    nombre: str
    apellido: str
    telefono: int
    direccion: str
    ciudad: str
    acompañante: str

# Modelo para la tabla "acompañante"
class Acompanante(BaseModel):
    nombre: str
    apellido: str
    telefono: int
    direccion: str
    parentezco: str
    identificacion: int
    id_paciente: int

# Modelo para la tabla "citas_medicas"
class CitaMedica(BaseModel):
    paciente: str
    acompañante: str
    fecha: str   
    hora: str   
    doctor: str
    sexo: str
    descripcion: str
    costo_cita: int
    id_paciente_acom: int

# Modelo para la tabla "doctores"
class Doctor(BaseModel):
    nombre: str
    apellido: str
    identificacion: int
    cuidad: str
    telefono: int
    gmail: str
    sexo: str
    edad: int
    titulo: str
    foto: Optional[bytes]  # Es opcional porque la foto puede ser NULL

# Modelo para la tabla "especialidades"
class Especialidad(BaseModel):
    especialidad: str
    id_doctor: int

# Modelo para la tabla "example"
class Examen(BaseModel):
    id_paciente: int
    id_doctor: int
    tipo: str
    costo: str
    fecha: str
    descripcion: str

# Modelo para la tabla "facture_citas"
class FacturaCita(BaseModel):
    id_citas_medicas: int
    fecha: str
    hora: str
    costo: int
    medio_pago: str
    estado: str

# Modelo para la tabla "facture_example"
class FacturaExamen(BaseModel):
    id_example: int
    fecha: str
    hora: str
    costo: int
    medio_pago: str
    estado: str

# Modelo para la tabla "usuarios"
class Usuario(BaseModel):
    usuario: str
    passw: str  # Evitar palabras reservadas como "pass"

# Modelo para la tabla "usuarios_nuevos"
class UsuarioNuevo(BaseModel):
    gmail: str
    usuario: str
    passw: str
 
 