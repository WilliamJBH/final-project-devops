import boto3
import os
from datetime import datetime

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET = 'devops-bucket-767398032096'

# 1. Subir archivo a S3
def subir_archivo(ruta_local, nombre_s3):
    s3.upload_file(ruta_local, BUCKET, nombre_s3)
    print(f"Archivo {nombre_s3} subido correctamente")

# 2. Listar objetos del bucket
def listar_objetos():
    print("\n=== Objetos en S3 ===")
    respuesta = s3.list_objects_v2(Bucket=BUCKET)
    if 'Contents' in respuesta:
        for obj in respuesta['Contents']:
            print(f"  {obj['Key']} | {obj['Size']} bytes | {obj['LastModified']}")
    else:
        print("  Bucket vacío")

# Crear archivo de prueba
with open('/tmp/prueba.txt', 'w') as f:
    f.write(f"Archivo de prueba generado: {datetime.now()}")

# Ejecutar funciones
subir_archivo('/tmp/prueba.txt', 'pruebas/prueba.txt')
listar_objetos()
