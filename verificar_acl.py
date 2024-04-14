#!/usr/bin/env python3
# Script para verificar tipo de ACL IPv4
numero_acl = input("Ingrese el número de ACL IPv4: ")
if numero_acl.isdigit():
    numero_acl = int(numero_acl)
    if numero_acl >= 1 and numero_acl <= 99:
        print("ACL Estándar")
    elif numero_acl >= 100 and numero_acl <= 199:
        print("ACL Extendida")
    else:
        print("No corresponde a una lista de acceso")
else:
    print("Ingrese un número válido")
