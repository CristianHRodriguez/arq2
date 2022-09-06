import psycopg2

# conexion BD
conexion = psycopg2.connect(user='ckzjgxztceaocn',
    password='3809a12da79c73515b63386e75ff8557fb7d495ee8143993b48510555d8cc51a',
    host='ec2-52-86-115-245.compute-1.amazonaws.com',
    port='5432',
    database='d4j126srukg58h')

cursor = conexion.cursor()

cursor = conexion.cursor()

sql = """UPDATE "Productos" SET "nombre"=%s, "precio"=%s, "categoria"=%s, "modelo"=%s, "talla"=%s, "color"=%s WHERE "ref"=%s"""

# consultar datos al usuario
ref = input("Ingrese referencia: ")
nombre = input('Ingrese nombre: ')
precio = input("Ingrese precio: ")
categoria = input("Ingrese categoria: ")
modelo = input('Ingrese modelo: ')
talla = input('Ingrese talla: ')
color = input("Ingrese color: ")

# recoleccion de datos
datos = (nombre, precio, categoria, modelo, talla, color, ref)

# hacer uso del metodo execute
cursor.execute(sql, datos)

# guardar registro
conexion.commit()

# registro insertados
actualizacion = cursor.rowcount

# Mostrar mensaje al usuario
print(f"Registro actualizado: {actualizacion}")

# cerrar conexiones
cursor.close()
conexion.close()
