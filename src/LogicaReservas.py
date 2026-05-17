# ================================================
# MÓDULO 2 — Lógica de Reservas
# Enoc Calzada | Grupo 3
# Depende de: modulo1.py (mesas) y modulo3.py (turnos)
# ================================================

from clientes_mesas import mesas
from infraestructura import mostrar_turnos, determinar_turno

# Lista donde se guardan todas las reservas
reservas = []


# ================================================
# CREAR RESERVA
# ================================================
def crear_reserva():
    print("\n===== NUEVA RESERVA =====")

    # Verificar que existan mesas registradas
    if len(mesas) == 0:
        print("ERROR: No hay mesas registradas. Registre mesas en el Módulo 1 primero.")
        return

    # Paso 1: Nombre del cliente
    nombre_cliente = input("Nombre del cliente: ").strip()
    if nombre_cliente == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    # Paso 2: Número de mesa
    try:
        numero_mesa = int(input("Número de mesa deseada: "))
    except ValueError:
        print("ERROR: Ingrese un número válido.")
        return

    # Validación 1: ¿La mesa existe?
    mesa_encontrada = next((m for m in mesas if m['numero'] == numero_mesa), None)
    if mesa_encontrada is None:
        print(f"ERROR: La mesa #{numero_mesa} no existe en el sistema.")
        return

    # Mostrar capacidad de la mesa encontrada
    print(f"La mesa #{numero_mesa} tiene capacidad para {mesa_encontrada['capacidad']} persona(s).")

    # Paso 3: Número de personas
    try:
        personas = int(input("Número de personas: "))
    except ValueError:
        print("ERROR: Ingrese un número válido.")
        return

    # Validación 2: ¿Hay capacidad suficiente?
    if personas <= 0:
        print("ERROR: El número de personas debe ser mayor a cero.")
        return
    if personas > mesa_encontrada['capacidad']:
        print(f"ERROR: Capacidad insuficiente.")
        print(f"La mesa #{numero_mesa} solo tiene capacidad para {mesa_encontrada['capacidad']} persona(s).")
        print(f"No se pueden acomodar {personas} personas en esta mesa.")
        return

    # Paso 4: Fecha
    fecha = input("Fecha de la reserva (DD/MM/AAAA): ").strip()
    if fecha == "":
        print("ERROR: La fecha no puede estar vacía.")
        return

    # Paso 5: Hora y asignación automática de turno
    mostrar_turnos()
    hora = input("Ingrese la hora de la reserva (formato HH:MM, ej: 14:30): ").strip()

    # Validación 3: ¿La hora corresponde a un turno válido?
    turno = determinar_turno(hora)
    if turno is None:
        print(f"ERROR: La hora {hora} no corresponde a ningún turno disponible.")
        mostrar_turnos()
        return

    print(f"Hora {hora} corresponde al turno: {turno}")

    # Validación 4: ¿Hay superposición de horarios?
    for r in reservas:
        if (r['numero_mesa'] == numero_mesa and
                r['fecha'] == fecha and
                r['turno'].upper() == turno.upper()):
            print(f"ERROR: Superposición detectada.")
            print(f"La mesa #{numero_mesa} ya tiene una reserva el {fecha} en el turno {turno}.")
            return

    # Guardar la reserva
    reservas.append({
        "cliente":     nombre_cliente,
        "numero_mesa": numero_mesa,
        "capacidad":   mesa_encontrada['capacidad'],
        "personas":    personas,
        "fecha":       fecha,
        "hora":        hora,
        "turno":       turno
    })

    print(f"\n¡Reserva registrada con éxito!")
    print(f"  Cliente : {nombre_cliente}")
    print(f"  Mesa    : #{numero_mesa} (Capacidad: {mesa_encontrada['capacidad']})")
    print(f"  Personas: {personas}")
    print(f"  Fecha   : {fecha}")
    print(f"  Turno   : {turno} ({hora})")


# ================================================
# VER TODAS LAS RESERVAS
# ================================================
def ver_reservas():
    print("\n===== RESUMEN DE RESERVAS =====")
    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return
    for i, r in enumerate(reservas, 1):
        print(f"\nReserva #{i}")
        print(f"  Cliente : {r['cliente']}")
        print(f"  Mesa    : #{r['numero_mesa']} (Capacidad: {r['capacidad']} personas)")
        print(f"  Personas: {r['personas']}")
        print(f"  Fecha   : {r['fecha']}")
        print(f"  Turno   : {r['turno']} ({r['hora']})")


# ================================================
# CANCELAR RESERVA
# ================================================
def cancelar_reserva():
    ver_reservas()
    if len(reservas) == 0:
        return
    try:
        numero = int(input("\nNúmero de reserva a cancelar: "))
        if numero < 1 or numero > len(reservas):
            print("ERROR: Número de reserva inválido.")
            return
        eliminada = reservas.pop(numero - 1)
        print(f"Reserva de {eliminada['cliente']} cancelada correctamente.")
    except ValueError:
        print("ERROR: Ingrese un número válido.")


# ================================================
# MENÚ DEL MÓDULO 2
# ================================================
def menu_modulo2():
    while True:
        print("\nMÓDULO DE RESERVAS")
        print("1. Crear reserva")
        print("2. Ver reservas")
        print("3. Cancelar reserva")
        print("4. Salir")

        op = input("Seleccione una opción: ")
        print()

        if op == "1":
            crear_reserva()
        elif op == "2":
            ver_reservas()
        elif op == "3":
            cancelar_reserva()
        elif op == "4":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_modulo2()