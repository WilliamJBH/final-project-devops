#!/bin/bash
echo "Instalando dependencias..."
sudo yum install -y git vim docker python3
sudo pip3 install boto3
sudo service docker start
echo "Dependencias instaladas correctamente."
