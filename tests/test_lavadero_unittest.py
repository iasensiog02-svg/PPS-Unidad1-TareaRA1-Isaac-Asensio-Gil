# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero desde el módulo padre
from lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        """Test 4: Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero._hacer_lavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------
        
    def test_estado_inicial(self):
        """Al crear el lavadero, todo debe estar a valores iniciales."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)
        
   
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero._hacer_lavado(False, False, True)
            
    def test3_lavadero_ocupado_lanza_error(self):
        self.lavadero.hacerLavado(False, False, False)
        with self.assertRaises(RuntimeError):
            self.lavadero.hacerLavado(False, False, False)

    def test_ingresos_prelavado(self):
        self._ejecutar_y_terminar(True, False, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.50)

    def test_ingresos_secado(self):
        self._ejecutar_y_terminar(False, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.00)

    def test_ingresos_secado_y_encerado(self):
        self._ejecutar_y_terminar(False, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.20)

    def test_ingresos_prelavado_y_secado(self):
        self._ejecutar_y_terminar(True, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.50)

    def test_ingresos_completo(self):
        self._ejecutar_y_terminar(True, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos,8.70)

    # ----------------------------------------------------------------------
    # Tests de flujo de fases
    # Utilizamos la función def ejecutar_y_obtener_fases(self, prelavado, secado, encerado)
    # Estos tests dan errores ya que en el código original hay errores en las las fases esperados, en los saltos.
    # ----------------------------------------------------------------------
    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
         
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
      
    def test_fases_sin_extras(self):
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        self.assertEqual(self._obtener_fases(False, False, False), fases_esperadas)

    def test_fases_con_prelavado(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        self.assertEqual(self._obtener_fases(True, False, False), fases_esperadas)

    def test_fases_con_secado(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        self.assertEqual(self._obtener_fases(False, True, False), fases_esperadas)

    def test_fases_con_secado_y_encerado(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        self.assertEqual(self._obtener_fases(False, True, True), fases_esperadas)

    def test_fases_prelavado_y_secado(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        self.assertEqual(self._obtener_fases(True, True, False), fases_esperadas)

    def test_fases_completo(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        self.assertEqual(self._obtener_fases(True, True, True), fases_esperadas)

 
# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()