import unittest
from unittest.mock import patch
import io
from clientes_mesas import clientes, mesas, registrar_clientes, editar_clientes, eliminar_cliente

class TestModuloRecepcion(unittest.TestCase):

    def setUp(self):
        """Este método corre ANTES de cada test para limpiar los datos globales."""
        clientes.clear()
        mesas.clear()

    #PRUEBAS DE REGISTRO

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Carlos', '123456', '5', 'n'])
    def test_registrar_cliente_exitoso(self, mock_input, mock_stdout):
        """Prueba registrar un cliente con una sola mesa con éxito."""
        registrar_clientes()
        
        self.assertEqual(len(clientes), 1)
        self.assertEqual(clientes[0]['nombre'], 'Carlos')
        self.assertIn(5, mesas)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['', '123456'])
    def test_registrar_cliente_nombre_vacio(self, mock_input, mock_stdout):
        """Prueba que no se registre si el nombre viene vacío."""
        registrar_clientes()
        self.assertEqual(len(clientes), 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Ana', '9876', '3', 's', '4', 'n'])
    def test_registrar_cliente_multiples_mesas(self, mock_input, mock_stdout):
        """Prueba registrar un cliente que pide más de una mesa."""
        registrar_clientes()
        self.assertEqual(clientes[0]['mesas_deseadas'], [3, 4])
        self.assertEqual(len(mesas), 2)

    #PRUEBAS DE EDICIÓN

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Juan']) 
    def test_editar_cliente_no_encontrado(self, mock_input, mock_stdout):
        """Prueba intentar editar un cliente que no existe."""
        editar_clientes() 
        self.assertEqual(len(clientes), 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Pedro', '3333-4444'])
    def test_editar_cliente_exitoso(self, mock_input, mock_stdout):
        """Prueba editar con éxito el teléfono de un cliente existente."""
        clientes.append({"nombre": "Pedro", "telefono": "5555-5555", "mesas_deseadas": [1]})
        
        editar_clientes()
        self.assertEqual(clientes[0]['telefono'], '3333-4444')

    #PRUEBAS DE ELIMINACIÓN

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Maria', 's']) 
    def test_eliminar_cliente_exitoso(self, mock_input, mock_stdout):
        """Prueba eliminar un cliente existente confirmando la acción."""
        clientes.append({"nombre": "Maria", "telefono": "1111-1111", "mesas_deseadas": [10, 11]})
        mesas.extend([10, 11])

        eliminar_cliente()
        
        self.assertEqual(len(clientes), 0)
        self.assertNotIn(10, mesas)
        self.assertNotIn(11, mesas)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Maria', 'n']) 
    def test_eliminar_cliente_cancelado(self, mock_input, mock_stdout):
        """Prueba cancelar la eliminación de un cliente."""
        clientes.append({"nombre": "Maria", "telefono": "1111-1111", "mesas_deseadas": [10]})
        mesas.append(10)

        eliminar_cliente()
        
        self.assertEqual(len(clientes), 1)
        self.assertIn(10, mesas)

if __name__ == '__main__':
    unittest.main()