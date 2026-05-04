import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Bienvenido a Soluciones Tecnologicas del Futuro",
        "Sistema operando correctamente",
        "Infraestructura DevOps activa",
        "Pipeline CI/CD funcionando",
        "Monitoreo CloudWatch activo"
    ]
    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': random.choice(mensajes),
            'servicio': 'microservicio-devops'
        })
    }
