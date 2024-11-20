
"""establecer conexion con la base de datos"""
import mysql.connector

conn = mysql.connector.connect(
        
    user= 'root',
    password ='1234',
    host='localhost',
    database='Gestion_citas'
)
cursor=conn.cursor()

