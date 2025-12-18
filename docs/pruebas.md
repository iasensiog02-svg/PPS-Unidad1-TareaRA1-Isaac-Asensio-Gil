# Ejecución y Depuración – Informe de Fallos

Durante el proceso de depuración se detectaron varios errores en el código y en los tests.  
A continuación se detallan uno por uno, con su explicación y la solución aplicada.

---

## Fallos y correcciones

1. **Clase Lavadero**
  * Se llamaba al método `_hacer_lavado` en lugar de `hacerLavado`.
  * **Corrección:** Cambiar la llamada a `self.lavadero.hacerLavado(...)`.

---

2. **Test 3**
  * Se lanzaba `ValueError` cuando debía ser `RuntimeError`.
  * **Corrección:** Sustituir la excepción por `RuntimeError`.
  
---

3. **Test 5**
  * Los ingresos esperados eran `6`.
  * El cálculo correcto es `6.20` (5.00 inicial + 1.20 coste de lavado).
  * **Corrección:** Cambiar ingresos esperados de `6` a `6.20`.

---

4. **Test 7**
   * Los ingresos esperados eran `7.50`.
   * Con prelavado a mano (1.50) y secado a mano (1.20), el total correcto es `7.70`.
   * **Corrección:** Cambiar ingresos esperados de `7.50` a `7.70`.

---

5. **Clase Lavadero – método `ejecutar_y_obtener_fases`**
   * El método estaba fuera de la clase por falta de tabulación.
   * **Corrección:** Añadir la indentación correcta para que quede dentro de la clase.

---

6. **Test 9**
   * `fases_esperadas = [0, 1, 3, 4, 5, 6, 0]`.
   * **Corrección:** Cambiar a `[0, 1, 3, 4, 5, 7, 0]`.

---

7. **Test 10**
   * `fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]`.
   * **Corrección:** Cambiar a `[0, 1, 2, 3, 4, 5, 7, 0]`.

---

8. **Test 11**
   * fases_esperadas = [0, 1, 3, 4, 5, 7, 0]`.
   * **Corrección:** Cambiar a `[0, 1, 3, 4, 5, 6, 0]`.

---

9. **Test 12**
   * `fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]`.
   * **Corrección:** Cambiar a `[0, 1, 3, 4, 5, 6, 0]`.

---

10. **Test 13**
    * `fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]`.
    * **Corrección:** Cambiar a `[0, 1, 2, 3, 4, 5, 6, 0]`.

---

11. **Test 14**
    * `fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]`.
    * **Corrección:** Cambiar a `[0, 1, 2, 3, 4, 5, 6, 0]`.

---

12. **Test 15**
    - Se llamaba a `self.lavadero.hacerLavado(False, False, True)`.
    - No se puede encerar el coche sin haber realizado el secado a mano.
    - **Corrección:** Cambiar a `self.lavadero.hacerLavado(False, True, True)`.

---

## Capturas de pantalla

![captura de test](Capturas/testok.png)

---
