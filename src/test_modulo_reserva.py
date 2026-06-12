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

mesas_prueba = [1, 2, 3]

# Simulamos las funciones del módulo 3
def mostrar_turnos_mock():
    print("\nDesayuno (07:00 - 12:00)")
    print("Almuerzo (12:00 - 19:00)")
    print("Cena     (19:00 - 22:00)")

def determinar_turno_mock(hora):
    if "07:00" <= hora < "12:00":
        return "Desayuno"
    elif "12:00" <= hora < "19:00":
        return "Almuerzo"
    elif "19:00" <= hora < "22:00":
        return "Cena"
    return None

# Aplicamos los mocks antes de importar el módulo
import sys
from unittest.mock import MagicMock

# Creamos módulos falsos
modulo1_mock = MagicMock()
modulo1_mock.clientes = clientes_prueba
modulo1_mock.mesas    = mesas_prueba

modulo3_mock = MagicMock()
modulo3_mock.mostrar_turnos  = mostrar_turnos_mock
modulo3_mock.determinar_turno = determinar_turno_mock

sys.modules['clientes_mesas']  = modulo1_mock
sys.modules['infraestructura'] = modulo3_mock

# Ahora sí importamos nuestro módulo
import LogicaReservas as mod2


# ================================================
# CLASE DE PRUEBAS
# ================================================

class TestLogicaReservas(unittest.TestCase):

    def setUp(self):
        """Limpia las reservas antes de cada prueba"""
        mod2.reservas.clear()
        mod2.clientes = clientes_prueba
        mod2.mesas    = mesas_prueba

    # ============================================
    # PRUEBAS: CREAR RESERVA
    # ============================================

    def test_01_crear_reserva_exitosa(self):
        """Una reserva válida se guarda correctamente"""
        inputs = ["Carlos", "1", "4", "14:00"]
        with patch("builtins.input", side_effect=inputs):
            mod2.crear_reserva()

        self.assertEqual(len(mod2.reservas), 1)
        self.assertEqual(mod2.reservas[0]['cliente'],     "Carlos")
        self.assertEqual(mod2.reservas[0]['numero_mesa'], 1)
        self.assertEqual(mod2.reservas[0]['capacidad'],   4)
        self.assertEqual(mod2.reservas[0]['turno'],       "Almuerzo")

    def test_02_crear_reserva_sin_clientes(self):
        """No se puede crear reserva si no hay clientes registrados"""
        mod2.clientes = []
        with patch("builtins.input", return_value=""):
            mod2.crear_reserva()

        self.assertEqual(len(mod2.reservas), 0)

    def test_03_cliente_no_existe(self):
        """Error si el cliente no está registrado en módulo 1"""
        with patch("builtins.input", return_value="UsuarioFalso"):
            mod2.crear_reserva()

        self.assertEqual(len(mod2.reservas), 0)

    def test_04_hora_invalida(self):
        """Error si la hora no corresponde a ningún turno"""
        inputs = ["Carlos", "1", "4", "23:00"]
        with patch("builtins.input", side_effect=inputs):
            mod2.crear_reserva()

        self.assertEqual(len(mod2.reservas), 0)

    def test_05_superposicion_mismo_turno(self):
        """No se puede reservar la misma mesa en el mismo turno dos veces"""
        # Primera reserva
        inputs1 = ["Carlos", "1", "4", "14:00"]
        with patch("builtins.input", side_effect=inputs1):
            mod2.crear_reserva()

        # Segunda reserva — misma mesa, mismo turno (Almuerzo)
        inputs2 = ["Maria", "1", "4", "13:00"]
        with patch("builtins.input", side_effect=inputs2):
            mod2.crear_reserva()

        # Solo debe haber 1 reserva guardada
        self.assertEqual(len(mod2.reservas), 1)

    def test_06_dos_reservas_diferente_turno(self):
        """La misma mesa puede reservarse en turnos distintos"""
        inputs1 = ["Carlos", "1", "4", "08:00"]
        with patch("builtins.input", side_effect=inputs1):
            mod2.crear_reserva()

        inputs2 = ["Maria", "1", "4", "14:00"]
        with patch("builtins.input", side_effect=inputs2):
            mod2.crear_reserva()

        self.assertEqual(len(mod2.reservas), 2)
        self.assertEqual(mod2.reservas[0]['turno'], "Desayuno")
        self.assertEqual(mod2.reservas[1]['turno'], "Almuerzo")

    # ============================================
    # PRUEBAS: EDITAR RESERVA — CAPACIDAD
    # ============================================

    def test_07_editar_capacidad(self):
        """Se puede cambiar la capacidad de una reserva existente"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })

        # Selecciona reserva 1, elige opción 1 (capacidad), nueva capacidad 8
        inputs = ["1", "1", "8"]
        with patch("builtins.input", side_effect=inputs):
            mod2.editar_reserva()

        self.assertEqual(mod2.reservas[0]['capacidad'], 8)

    def test_08_editar_capacidad_invalida(self):
        """La capacidad no puede ser cero ni negativa"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })

        # Intenta poner capacidad 0 primero, luego pone 5
        inputs = ["1", "1", "0", "5"]
        with patch("builtins.input", side_effect=inputs):
            mod2.editar_reserva()

        self.assertEqual(mod2.reservas[0]['capacidad'], 5)

    # ============================================
    # PRUEBAS: EDITAR RESERVA — HORARIO
    # ============================================

    def test_09_editar_horario(self):
        """Se puede cambiar el horario de una reserva existente"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })

        # Selecciona reserva 1, elige opción 2 (horario), nueva hora 20:00
        inputs = ["1", "2", "20:00"]
        with patch("builtins.input", side_effect=inputs):
            mod2.editar_reserva()

        self.assertEqual(mod2.reservas[0]['hora'],  "20:00")
        self.assertEqual(mod2.reservas[0]['turno'], "Cena")

    def test_10_editar_horario_superposicion(self):
        """No se puede mover una reserva a un turno ya ocupado en la misma mesa"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })
        mod2.reservas.append({
            "cliente": "Maria", "telefono": "555-5678",
            "numero_mesa": 1, "capacidad": 3,
            "hora": "20:00", "turno": "Cena"
        })

        # Intenta mover la reserva 1 al turno Cena (ya ocupado)
        inputs = ["1", "2", "20:00"]
        with patch("builtins.input", side_effect=inputs):
            mod2.editar_reserva()

        # El horario de la reserva 1 NO debe haber cambiado
        self.assertEqual(mod2.reservas[0]['turno'], "Almuerzo")

    def test_11_editar_horario_invalido(self):
        """Error si la nueva hora no corresponde a ningún turno"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })

        inputs = ["1", "2", "23:00"]
        with patch("builtins.input", side_effect=inputs):
            mod2.editar_reserva()

        # El horario no debe cambiar
        self.assertEqual(mod2.reservas[0]['hora'], "14:00")

    # ============================================
    # PRUEBAS: CANCELAR RESERVA
    # ============================================

    def test_12_cancelar_reserva(self):
        """Se puede eliminar una reserva existente"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })

        with patch("builtins.input", return_value="1"):
            mod2.cancelar_reserva()

        self.assertEqual(len(mod2.reservas), 0)

    def test_13_cancelar_reserva_invalida(self):
        """Error si el número de reserva no existe"""
        mod2.reservas.append({
            "cliente": "Carlos", "telefono": "555-1234",
            "numero_mesa": 1, "capacidad": 4,
            "hora": "14:00", "turno": "Almuerzo"
        })

        # Intenta cancelar la reserva número 99 que no existe
        with patch("builtins.input", return_value="99"):
            mod2.cancelar_reserva()

        # La reserva debe seguir existiendo
        self.assertEqual(len(mod2.reservas), 1)


# ================================================
# EJECUTAR PRUEBAS
# ================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)