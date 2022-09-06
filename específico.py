import psycopg2

# conexion BD
conexion = psycopg2.connect(user='ckzjgxztceaocn',
    password='3809a12da79c73515b63386e75ff8557fb7d495ee8143993b48510555d8cc51a',
    host='ec2-52-86-115-245.compute-1.amazonaws.com',
    port='5432',
    database='d4j126srukg58h')

cursor = conexion.cursor()

cursor = conexion.cursor()

# Crear la sentencia SQL
sql = """SELECT * FROM "Productos" WHERE "ref"=%s"""

# Solicitar dato al usuario
ref = input("Ingrese la referencia deseada: ")

# Uso del metodo execute
cursor.execute(sql, ref)

# Mostrar resultado
registro = cursor.fetchone()

# Mostrar en consola
print(registro)

# Cerrar conexion
cursor.close()
conexion.close()
