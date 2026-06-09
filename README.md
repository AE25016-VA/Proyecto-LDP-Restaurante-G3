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

### 1. Clonar el Repositorio
Abra la terminal de su sistema operativo y ejecute el siguiente comando para clonar el proyecto:
```bash
git clone https://github.com/AE25016-VA/Proyecto-LDP-Restaurante-G3.git
