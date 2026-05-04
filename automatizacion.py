import boto3
import json
from datetime import datetime, timedelta

# Cliente EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

# Cliente CloudWatch
cw = boto3.client('cloudwatch', region_name='us-east-1')

# Cliente S3
s3 = boto3.client('s3', region_name='us-east-1')

# 1. Listar instancias EC2
print("\n=== Instancias EC2 ===")
respuesta = ec2.describe_instances()
for reserva in respuesta['Reservations']:
    for instancia in reserva['Instances']:
        print(f"ID: {instancia['InstanceId']} | Tipo: {instancia['InstanceType']} | Estado: {instancia['State']['Name']}")

# 2. Reporte de uso de recursos EC2
print("\n=== Reporte de uso de CPU (ultimas 24 horas) ===")
instancias = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for reserva in instancias['Reservations']:
    for instancia in reserva['Instances']:
        instance_id = instancia['InstanceId']
        metricas = cw.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=datetime.utcnow() - timedelta(hours=24),
            EndTime=datetime.utcnow(),
            Period=3600,
            Statistics=['Average']
        )
        print(f"Instancia: {instance_id} | Puntos de datos CPU: {len(metricas['Datapoints'])}")

# 3. Listar buckets S3 y objetos
print("\n=== Buckets S3 ===")
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"Bucket: {bucket['Name']}")
    try:
        objetos = s3.list_objects_v2(Bucket=bucket['Name'])
        if 'Contents' in objetos:
            for obj in objetos['Contents']:
                print(f"  Objeto: {obj['Key']} | Tamanio: {obj['Size']} bytes")
        else:
            print("  Sin objetos")
    except Exception as e:
        print(f"  Sin acceso: {e}")

print("\n=== Reporte generado:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "===")

# 4. Gestionar reglas de autoescalado
print("\n=== Grupos de Auto Scaling ===")
asg = boto3.client('autoscaling', region_name='us-east-1')
grupos = asg.describe_auto_scaling_groups()
if grupos['AutoScalingGroups']:
    for grupo in grupos['AutoScalingGroups']:
        print(f"Grupo: {grupo['AutoScalingGroupName']} | Min: {grupo['MinSize']} | Max: {grupo['MaxSize']} | Deseado: {grupo['DesiredCapacity']}")
else:
    print("No hay grupos de Auto Scaling configurados")
