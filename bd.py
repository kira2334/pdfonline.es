import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                           user='admin_pdfonline',
                           password='root@',
                           db='pdfonline.es')
