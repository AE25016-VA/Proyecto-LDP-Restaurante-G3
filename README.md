# Sistema Integrado de Reservas de Restaurante - Grupo 3
Este es el proyecto final para la asignatura de **Lógica de Programación**. Consiste en una aplicación de interfaz de línea de comandos (CLI) desarrollada en Python, diseñada para automatizar y coordinar las operaciones lógicas, asignación de mesas y control de turnos en un restaurante en tiempo real.
El proyecto partió de una fase previa de abstracción en pseudocódigo (`docs/pseudocodigo`) y ha evolucionado hacia un software modularizado e interconectado, garantizando el manejo robusto de excepciones y la persistencia de datos.

## Integrantes del Equipo y Roles

* **Vanessa Gabriela Arévalo Elías** (`@AE25016-VA`) - **Coordinadora** | Desarrollo del Módulo 1: Recepción, Clientes y Mesas Deseadas.
* **Carlos Enoc Calzada Vargas** (`@cv19058`) | Desarrollo del Módulo 2: Lógica, Asignación y Gestión de Reservas.
* **Rafael Antonio Cerritos Acosta** (`@CA25045`) | Desarrollo del Módulo 3: Infraestructura, Control de Turnos e Informes Históricos.

## Arquitectura del Repositorio

El proyecto se compone en las siguientes carpetas:
* `src/`: Contiene el código fuente ejecutable en Python.
    * `main.py`: Orquestador central de la CLI y punto de entrada del sistema.
    * `clientes_mesas.py`: Lógica de datos maestros para pre-registro de clientes.
    * `LogicaReservas.py`: Validación y control de colisiones en reservas.
    * `infraestructura.py`: Gestión horaria de turnos y persistencia en archivos JSON.
    * `test_proyecto.py`: Set de pruebas unitarias automatizadas del sistema.
* `docs/pseudocodigo/`: Contiene los algoritmos iniciales desarrollados en PSeInt (`.psc`), sirviendo como bitácora de diseño lógico original.

## Instrucciones de Ejecución

Siga estos pasos para clonar, iniciar y probar la aplicación CLI en su entorno local:

### Clonar el Repositorio
Abra la terminal de su sistema operativo y ejecute el siguiente comando para clonar el proyecto:
```bash
git clone [https://github.com/TU_USUARIO/Proyecto-LDP-Restaurante-G3.git](https://github.com/TU_USUARIO/Proyecto-LDP-Restaurante-G3.git)
cd Proyecto-LDP-Restaurante-G3
```
### Iniciar la Aplicación (main.py)
Para ejecutar la solución definitiva e interactuar con la interfaz del sistema, ejecute el archivo unificador central con el siguiente comando:
python src/main.py

## Pasos para Probar la Demo en la Presentación
Para demostrar el correcto funcionamiento e integración de los módulos en tiempo real frente al evaluador, ejecute el programa interactivo siguiendo estrictamente este orden lógico en la terminal:

* Paso 1: Pre-registro de Clientes y Preferencias (Módulo 1)
   * En el Menú Principal, ingrese seleccionando la Opción 1.
   * Rellene los datos básicos solicitados en la terminal: Nombre y Teléfono del cliente.
   * El sistema le consultará el número de mesa que el cliente desea registrar originalmente.
   * Tras confirmar la primera mesa, el sistema le preguntará si prefiere añadir más mesas a sus preferencias. Al terminar, el flujo guardará los datos en memoria y regresará de forma limpia al Menú Principal.

* Paso 2: Formalización y Validación de la Reserva (Módulo 2)
   * En el Menú Principal, ingrese seleccionando la Opción 2.
   * Digite el nombre exacto del cliente que pre-registró en el Paso 1.
   * El sistema buscará en la memoria y desplegará automáticamente en pantalla la lista de mesas que ese usuario desea registrar.
   * Proceda con la asignación ingresando los detalles de la reserva: Cantidad de personas y la Hora de la reserva.
   * El sistema validará internamente que las capacidades sean coherentes y clasificará de manera dinámica la reserva en el horario correspondiente (Desayuno, Almuerzo o Cena), guardándola con éxito.

* Paso 3: Visualización del Reporte General del Sistema
   * Regrese una vez más al Menú Principal y elija la Opción 4 (Ver Reporte General del Sistema).
   * Podrá examinar el balance consolidado del restaurante en tiempo real, verificando la persistencia integrada de los datos: el número total de clientes guardados por el Módulo 1 y el desglose de las reservas activas procesadas por el Módulo 2 con sus respectivos turnos.

## Manejo de Errores y Robustez
El sistema cuenta con validaciones mediante bloques de control de excepciones try-except para garantizar estabilidad ante entradas inválidas:

* Evita cierres inesperados si se digitan letras en campos estrictamente numéricos (opciones de menús, números de mesa o cantidad de comensales).
* Controla que los nombres ingresados no sean cadenas vacías.
* Restringe la entrada de capacidades o números de personas menores o iguales a cero.

## Pruebas Unitarias Automatizadas (Unittest)
En cumplimiento con las exigencias de control de calidad de la entrega final, el software incorpora una batería de pruebas automáticas utilizando el framework nativo unittest de Python.
Para ejecutar todas las pruebas unitarias y verificar la integridad de la lógica de negocio directamente desde la consola, ejecute:

* Modulo 1:
```bash
python -m unittest discover -s src -p "test_modulo1.py"
```
* Modulo 2:
```bash
python -m unittest discover -s src -p "test_modulo_reserva.py"
```
* Modulo 3:

* Todos los test:
```bash
python -m unittest discover -s src -p "test_*.py"
```
