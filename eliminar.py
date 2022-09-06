import psycopg2

# conexion BD
conexion = psycopg2.connect(user='ckzjgxztceaocn',
    password='3809a12da79c73515b63386e75ff8557fb7d495ee8143993b48510555d8cc51a',
    host='ec2-52-86-115-245.compute-1.amazonaws.com',
    port='5432',
    database='d4j126srukg58h')

cursor = conexion.cursor()

cursor = conexion.cursor()

# utilizar cursor
cursor = conexion.cursor()

# Sentencia SQL
sql = """DELETE FROM "Productos" WHERE "ref"=%s"""

# Solicitar dato al usuario
ref_media_delete = input("Referencia a eliminar: ")

# metodo execute
cursor.execute(sql, ref_media_delete)

# guardar cambios
conexion.commit()

# conteo de registro eliminado
referencia_deleted = cursor.rowcount

# mensaje al usuario
print(f'Registro eliminado: {referencia_deleted}')

# Cerrar conexion
cursor.close()
conexion.close()
