#!/bin/bash
echo "Iniciando limpieza de logs..."
find /var/log -name "*.log" -mtime +7 -delete
echo "Limpieza completada: $(date)"
