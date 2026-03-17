import mysql.connector
dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)
## Preparar un cursos para filas y columnas.
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE cliente")
print("Base de datos creada con exito")