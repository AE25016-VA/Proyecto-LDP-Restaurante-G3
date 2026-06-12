import unittest
from unittest.mock import patch

# ================================================
# SIMULAMOS los módulos de los compañeros
# para que las pruebas corran solas sin depender
# de los archivos de Vanessa y Rafael
# ================================================

# Datos de prueba que simulan el módulo 1
clientes_prueba = [
    {
        "nombre": "Carlos",
        "telefono": "555-1234",
        "mesas_deseadas": [1, 2]
    },
    {
        "nombre": "Maria",
        "telefono": "555-5678",
        "mesas_deseadas": [3]
    }
]