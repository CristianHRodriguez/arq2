import psycopg2

# conexion BD
conexion = psycopg2.connect(user='ckzjgxztceaocn',
    password='3809a12da79c73515b63386e75ff8557fb7d495ee8143993b48510555d8cc51a',
    host='ec2-52-86-115-245.compute-1.amazonaws.com',
    port='5432',
    database='d4j126srukg58h')

cursor = conexion.cursor()

sql = """INSERT INTO "Productos"("nombre", "precio", "categoria", "modelo", "talla", "color") VALUES(%s, %s, %s, %s, %s, %s)"""

print('Describa el producto')
ref = input("Ingrese referencia: ")
nombre = input('Ingrese nombre: ')
precio = input("Ingrese precio: ")
categoria = input("Ingrese categoria: ")
modelo = input('Ingrese modelo: ')
talla = input('Ingrese talla: ')
color = input("Ingrese color: ")

datos = (nombre, precio, categoria, modelo, talla, color)

cursor.execute(sql, datos)

conexion.commit()

registros = cursor.rowcount

print('registro insertado: ', registros)

cursor.close()
conexion.close()