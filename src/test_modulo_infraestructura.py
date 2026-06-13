import unittest
from unittest.mock import patch
import io
import os

from infraestructura import (
    determinar_turno,
    guardar_mesas,
    cargar_mesas,
    reporte_infraestructura
)


class TestModuloInfraestructura(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba."""
        if os.path.exists("mesas.json"):
            os.remove("mesas.json")

    def tearDown(self):
        """Se ejecuta después de cada prueba."""
        if os.path.exists("mesas.json"):
            os.remove("mesas.json")

    # ============================================
    # PRUEBAS DE TURNOS
    # ============================================

    def test_turno_desayuno(self):
        self.assertEqual(
            determinar_turno("08:00"),
            "Desayuno"
        )

    def test_turno_almuerzo(self):
        self.assertEqual(
            determinar_turno("14:00"),
            "Almuerzo"
        )

    def test_turno_cena(self):
        self.assertEqual(
            determinar_turno("20:00"),
            "Cena"
        )

    def test_turno_invalido(self):
        self.assertIsNone(
            determinar_turno("23:00")
        )

    # ============================================
    # PRUEBAS DE PERSISTENCIA
    # ============================================

    def test_guardar_y_cargar_mesas(self):

        mesas_prueba = [
            {"numero": 1, "capacidad": 4},
            {"numero": 2, "capacidad": 6}
        ]

        guardar_mesas(mesas_prueba)

        resultado = cargar_mesas()

        self.assertEqual(
            resultado,
            mesas_prueba
        )

    def test_cargar_sin_archivo(self):

        resultado = cargar_mesas()

        self.assertEqual(
            resultado,
            []
        )

    # ============================================
    # PRUEBAS DE REPORTE
    # ============================================

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_reporte_sin_mesas(
        self,
        mock_stdout
    ):

        reporte_infraestructura([])

        salida = mock_stdout.getvalue()

        self.assertIn(
            "REPORTE INFRAESTRUCTURA",
            salida
        )

        self.assertIn(
            "No hay mesas registradas",
            salida
        )

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_reporte_con_mesas(
        self,
        mock_stdout
    ):

        mesas = [
            {
                "numero": 1,
                "capacidad": 4
            }
        ]

        reporte_infraestructura(mesas)

        salida = mock_stdout.getvalue()

        self.assertIn(
            "Mesa #1",
            salida
        )

        self.assertIn(
            "Total de mesas: 1",
            salida
        )


if __name__ == "__main__":
    unittest.main()
