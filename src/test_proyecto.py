# src/test_proyecto.py
import unittest
from clientes_mesas import clientes, mesas 
from LogicaReservas import reservas

class TestRestaurante(unittest.TestCase):

    def setUp(self):
        """Este método limpia las listas antes de cada prueba para que no se mezclen datos"""
        clientes.clear()
        mesas.clear()
        reservas.clear()

    # 1. PRUBA De Módulo 1
    def test_registro_cliente_y_mesas_deseadas(self):
        
        clientes.append({
            "nombre": "Vanessa",
            "telefono": "7777-7777",
            "mesas_deseadas": [5, 3]  
        })
        
       
        mesas.append(5)
        mesas.append(3)

        self.assertEqual(len(clientes), 1)
        self.assertIn(5, mesas)  
        self.assertEqual(clientes[0]["nombre"], "Vanessa")
        self.assertIsInstance(clientes[0]["mesas_deseadas"], list)

    # 2. PRUEBA De Módulo 2
    def test_estructura_reserva_vacia_al_inicio(self):
        self.assertIsInstance(reservas, list)
        self.assertEqual(len(reservas), 0)

    # 3. PRUEBA DE CONTROL DE CAPACIDAD (Lógica de validación)
    def test_validacion_capacidad_reserva_positiva(self):
        reservas.append({
            "cliente": "Vanessa",
            "numero_mesa": 5,
            "capacidad": 4, 
            "hora": "13:00",
            "turno": "Almuerzo"
        })
        
        self.assertTrue(reservas[0]["capacidad"] > 0)
        self.assertEqual(reservas[0]["turno"], "Almuerzo")

if __name__ == "__main__":
    unittest.main()