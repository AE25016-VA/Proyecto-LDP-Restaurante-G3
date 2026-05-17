from clientes_mesas import mesas, clientes 
from infraestructura import mostrar_turnos, determinar_turno

# Lista donde se guardan todas las reservas
reservas = []


# CREAR RESERVA
def crear_reserva():
    print("\n===== ASIGNACIÓN Y DETALLES DE RESERVAS =====")

    # Verificar que existan clientes registrados
    if len(clientes) == 0:
        print("ERROR: No hay clientes registrados. Regístrelos en el Módulo 1 primero.")
        return
    
    nombre_buscar = input("Ingrese el nombre del cliente pre-registrado: ").strip()
    cliente_encontrado = next((c for c in clientes if c['nombre'].upper() == nombre_buscar.upper()), None)

    if not cliente_encontrado:
        print("ERROR: Cliente no encontrado en el sistema. Debe registrarse en el Módulo 1.")
        return
    
    print(f"Mesas que este cliente solicitó originalmente: {cliente_encontrado['mesas_deseadas']}")

    try:
        # 2. Validar Número de Mesa
        numero_mesa = int(input("Confirme el número de mesa a asignar: "))
        if numero_mesa not in cliente_encontrado['mesas_deseadas']:
            print("AVISO: Esta mesa no estaba en sus opciones deseadas, pero se procesará.")

        # 3. Validar Capacidad (No negativa ni cero)
        capacidad = 0
        while capacidad <= 0:
            capacidad = int(input("Ingrese la capacidad para la mesa: "))
            if capacidad <= 0:
                print("ERROR: La capacidad debe ser un número positivo mayor a cero.")

        # 4. Detalles del Horario y Turno
        print("\nHorarios disponibles del restaurante:")
        mostrar_turnos()
        hora = input("\nIngrese la hora (HH:MM): ").strip()
        
        turno = determinar_turno(hora)
        if turno is None:
            print("ERROR: La hora ingresada no coincide con ningún turno (Desayuno, Almuerzo, Cena).")
            return

        # Guardar reserva formalizada respetando datos
        reservas.append({
            "cliente": cliente_encontrado['nombre'],
            "telefono": cliente_encontrado['telefono'],
            "numero_mesa": numero_mesa,
            "capacidad": capacidad,
            "hora": hora,
            "turno": turno
        })
        print(f"¡Reserva confirmada con éxito para {cliente_encontrado['nombre']} en el turno {turno}!")

    except ValueError:
        print("ERROR: Entrada de datos numérica inválida.")


def ver_reservas():
    print("\n===== LISTA DE RESERVAS ACTIVAS =====")
    if len(reservas) == 0:
        print("No hay reservas confirmadas.")
        return
    for idx, r in enumerate(reservas, 1):
        print(f"\n[{idx}] Cliente: {r['cliente']} | Teléfono: {r['telefono']}")
        print(f"    Mesa Asignada: #{r['numero_mesa']} | Capacidad de Mesa: {r['capacidad']} personas")
        print(f"    Horario: {r['hora']} | Corresponde a: {r['turno']}")

def editar_reserva():
    ver_reservas()
    if len(reservas) == 0:
        return
    try:
        idx = int(input("\nSeleccione el número de la reserva que desea editar: ")) - 1
        if idx < 0 or idx >= len(reservas):
            print("ERROR: Selección inválida.")
            return
        
        print(f"Modificando la reserva de {reservas[idx]['cliente']}:")
        
        # Alterar la capacidad validando que no sea cero ni negativa
        nueva_capacidad = 0
        while nueva_capacidad <= 0:
            nueva_capacidad = int(input("Ingrese la nueva capacidad de la mesa (mayor a 0): "))
            if nueva_capacidad <= 0:
                print("ERROR: No puede ser cero ni negativo.")
                
        reservas[idx]['capacidad'] = nueva_capacidad
        print("¡Capacidad de la reserva alterada y actualizada con éxito!")
        
    except ValueError:
        print("ERROR: Ingrese un número válido.")

def cancelar_reserva():
    ver_reservas()
    if len(reservas) == 0:
        return
    try:
        numero = int(input("\nNúmero de reserva a cancelar: "))
        if numero < 1 or numero > len(reservas):
            print("ERROR: Número inválido.")
            return
        eliminada = reservas.pop(numero - 1)
        print(f"La reserva de {eliminada['cliente']} para la Mesa #{eliminada['numero_mesa']} fue eliminada.")
    except ValueError:
        print("ERROR: Ingrese un número válido.")

def menu_modulo2():
    while True:
        print("\n--- MÓDULO 2: GESTIÓN DE RESERVAS ---")
        print("1. Confirmar y Completar Reserva")
        print("2. Ver todas las Reservas")
        print("3. Editar Reserva (Alterar Capacidad)")
        print("4. Cancelar Reserva")
        print("5. Salir al Menú Principal")

        op = input("Seleccione una opción: ")
        if op == "1": crear_reserva()
        elif op == "2": ver_reservas()
        elif op == "3": editar_reserva()
        elif op == "4": cancelar_reserva()
        elif op == "5": break