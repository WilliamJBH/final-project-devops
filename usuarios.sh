#!/bin/bash
echo "Gestion de usuarios y permisos"

# Crear usuario
sudo useradd -m devops_user
echo "Usuario devops_user creado"

# Asignar permisos a carpeta del proyecto
sudo chown -R devops_user:devops_user ~/environment
echo "Permisos asignados a ~/environment"

# Crear grupo devops
sudo groupadd devops_group
sudo usermod -aG devops_group devops_user
echo "Usuario agregado al grupo devops_group"

echo "Gestion completada."
sudo chown -R ec2-user:ec2-user ~/environment
