import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
client = boto3.client('dynamodb', region_name='us-east-1')

TABLA = 'devops-tabla'

# 1. Crear tabla
def crear_tabla():
    try:
        tabla = dynamodb.create_table(
            TableName=TABLA,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        tabla.wait_until_exists()
        print(f"Tabla {TABLA} creada correctamente")
    except client.exceptions.ResourceInUseException:
        print(f"Tabla {TABLA} ya existe")

# 2. Insertar registro
def insertar_registro():
    tabla = dynamodb.Table(TABLA)
    tabla.put_item(Item={'id': '001', 'nombre': 'Soluciones Tecnologicas', 'status': 'activo'})
    print("Registro insertado correctamente")

# 3. Modificar registro
def modificar_registro():
    tabla = dynamodb.Table(TABLA)
    tabla.update_item(
        Key={'id': '001'},
        UpdateExpression='SET #s = :val',
        ExpressionAttributeNames={'#s': 'status'},
        ExpressionAttributeValues={':val': 'inactivo'}
    )
    print("Registro modificado correctamente")

# 4. Eliminar registro
def eliminar_registro():
    tabla = dynamodb.Table(TABLA)
    tabla.delete_item(Key={'id': '001'})
    print("Registro eliminado correctamente")

# Ejecutar operaciones
crear_tabla()
insertar_registro()
modificar_registro()
eliminar_registro()
print("\nOperaciones DynamoDB completadas.")
