CREATE DATABASE gestion_citas;
USE gestion_citas;

CREATE TABLE pacientes (
  id_pacientes INT PRIMARY KEY IDENTITY(1,1),
  nombre NVARCHAR(20) NOT NULL,
  apellido NVARCHAR(20) NOT NULL,
  telefono BIGINT NOT NULL,
  direccion NVARCHAR(20) NOT NULL,
  ciudad NVARCHAR(20) NOT NULL,
  acompañante NVARCHAR(20) NOT NULL
);

CREATE TABLE acompañante (
  id_acom INT PRIMARY KEY IDENTITY(1,1),
  nombre NVARCHAR(20) NOT NULL,
  apellido NVARCHAR(20) NOT NULL,
  telefono BIGINT NOT NULL,
  direccion NVARCHAR(20) NOT NULL,
  parentezco NVARCHAR(20) NOT NULL,
  identificacion BIGINT NOT NULL,
  id_paciente INT NOT NULL,
  FOREIGN KEY (id_paciente) REFERENCES pacientes(id_pacientes)
);

CREATE TABLE citas_medicas (
  id_citas INT PRIMARY KEY IDENTITY(1,1),
  paciente NVARCHAR(20) NOT NULL,
  acompañante NVARCHAR(20) NOT NULL,
  fecha DATE NOT NULL,
  hora TIME NOT NULL,
  doctor NVARCHAR(20) NOT NULL,
  sexo NVARCHAR(10) NOT NULL,
  descripcion NVARCHAR(60) NOT NULL,
  costo_cita INT NOT NULL,
  id_paciente_acom INT NOT NULL,
  FOREIGN KEY (id_paciente_acom) REFERENCES pacientes(id_pacientes)
);

CREATE TABLE doctores (
  id_doctor INT PRIMARY KEY IDENTITY(1,1),
  nombre NVARCHAR(20) NOT NULL,
  apellido NVARCHAR(20) NOT NULL,
  identificacion BIGINT NOT NULL,
  cuidad NVARCHAR(20) NOT NULL,
  telefono BIGINT NOT NULL,
  gmail NVARCHAR(50) NOT NULL,
  sexo NVARCHAR(15) NOT NULL,
  edad INT NOT NULL,
  titulo NVARCHAR(20) NOT NULL,
  foto VARBINARY(MAX) NULL
);

CREATE TABLE especialidades (
  id_es INT PRIMARY KEY IDENTITY(1,1),
  especialidad NVARCHAR(20) NOT NULL,
  id_doctor INT NOT NULL,
  FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor)
);

CREATE TABLE example (
  id_exam INT PRIMARY KEY IDENTITY(1,1),
  id_paciente INT NOT NULL,
  id_doctor INT NOT NULL,
  tipo NVARCHAR(20) NOT NULL,
  costo NVARCHAR NOT NULL,
  fecha DATE NOT NULL,
  descripcion NVARCHAR(500) NOT NULL,
  FOREIGN KEY (id_paciente) REFERENCES pacientes(id_pacientes),
  FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor)
);

CREATE TABLE facture_citas (
  id_fac_citas INT PRIMARY KEY IDENTITY(1,1),
  id_citas_medicas INT NOT NULL,
  fecha DATE NOT NULL,
  hora TIME NOT NULL,
  costo INT NOT NULL,
  medio_pago NVARCHAR(15) NOT NULL,
  estado NVARCHAR(20) NOT NULL,
  FOREIGN KEY (id_citas_medicas) REFERENCES citas_medicas(id_citas)
);

CREATE TABLE facture_example (
  id_fact INT PRIMARY KEY IDENTITY(1,1),
  id_example INT NOT NULL,
  fecha DATE NOT NULL,
  hora TIME NOT NULL,
  costo INT NOT NULL,
  medio_pago NVARCHAR(15) NOT NULL,
  estado NVARCHAR(20) NOT NULL,
  FOREIGN KEY (id_example) REFERENCES example(id_exam)
);


CREATE TABLE usuarios (
  id_user INT PRIMARY KEY IDENTITY(1,1),
  usuario NVARCHAR(20) NOT NULL,
  pass NVARCHAR(20) NOT NULL
);

CREATE TABLE usuarios_nuevos (
  id_new INT PRIMARY KEY IDENTITY(1,1),
  gmail NVARCHAR(50) NOT NULL,
  usuario NVARCHAR(20) NOT NULL,
  pass NVARCHAR(20) NOT NULL
);

SELECT * FROM doctores;

ALTER TABLE doctores
ADD  foto VARBINARY(MAX) NULL;

