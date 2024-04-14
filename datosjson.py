#!/usr/bin/env python3
import json

# Abrir y cargar el archivo JSON
with open('myfile.json') as json_file:
    json_data = json.load(json_file)

# Imprimir el valor del token y tiempo restante
print("Valor del token:", json_data['token'])
print("Tiempo restante antes de caducar:", json_data['tiempo_restante'])
