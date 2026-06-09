# Comenzar el módulo
clientes = []
mesas = []

# Clientes 
def registrar_clientes():
    print("\nREGISTRO DE CLIENTE Y MESA")
    nombre = input("Ingrese nombre del cliente: ")
    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    if any(c['nombre'].upper() == nombre.upper() for c in clientes):
        print("ERROR: Este cliente ya está registrado.")
        return
    
    telefono = input(f"Ingrese el número del teléfono de {nombre}: ")
    mesas_cliente = []

    while True:
        try:
            mesa = int(input("Ingrese el número de mesa que desea reservar: "))
            
            if mesa in mesas_cliente:
                print("Ya has solicitado esta mesa para este cliente.")
            else:
                mesas_cliente.append(mesa)
                mesas.append(mesa) 
                print(f"Mesa {mesa} agregada.")
            
            resp = input("¿Desea añadir otra mesa deseada? (s/n): ").strip().lower()
            if resp != 's':
                break
                
        except ValueError:
            print("ERROR: Ingrese un número de mesa válido.")
            if not mesas_cliente:
                resp = input("No se han guardado mesas. ¿Desea intentar de nuevo? (s/n): ").strip().lower()
                if resp != 's':
                    print("Registro cancelado.")
                    return

    if mesas_cliente:
        clientes.append({
            "nombre": nombre,
            "telefono": telefono,
            "mesas_deseadas": mesas_cliente
        })
        print(f"\nPre-registro de {nombre} guardado con éxito con las mesas: {mesas_cliente}")

def editar_clientes():
    nombre_buscar = input("Nombre del cliente a editar: ")
    for cliente in clientes:
        if cliente['nombre'].upper() == nombre_buscar.upper():
            cliente['telefono'] = input("Nuevo teléfono: ")
            print("Datos actualizados.")
            return
    print("Cliente no encontrado.")

def eliminar_cliente():
    nombre_buscar = input("Nombre del cliente a eliminar: ")
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['nombre'].upper() == nombre_buscar.upper():
            cliente_encontrado = cliente
            break
            
    if cliente_encontrado:
        confirmacion = input(f"¿Está seguro que quiere eliminar a {cliente_encontrado['nombre']}? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            for mesa in cliente_encontrado['mesas_deseadas']:
                if mesa in mesas:
                    mesas.remove(mesa)
            
            clientes.remove(cliente_encontrado)
            print(f"El cliente {cliente_encontrado['nombre']} y sus peticiones de mesas han sido eliminados con éxito.")
        else:
            print("Eliminación cancelada.")
    else:
        print("Cliente no encontrado.")
              
def listar_todo():
    print("\n=== RESUMEN FINAL ===")
    print("Clientes registrados:")
    if not clientes:
        print("  (No hay clientes)")
    for c in clientes:
        print(f"  - {c['nombre']} (Tel: {c['telefono']}) -> Mesas: {c['mesas_deseadas']}")
    print("Lista global de todas las mesas reservadas:", mesas)

# Menú de prueba
def menu_modulo1():
    while True:
        print("\nMÓDULO 1: RECEPCIÓN Y CLIENTES")  
        print("1. Registrar Cliente y Mesas Deseadas")
        print("2. Editar Cliente")
        print("3. Eliminar Cliente")
        print("4. Ver todo")
        print("5. Salir al Menú Principal")
        op = input("Seleccione una opción: ")

        if op == "1": registrar_clientes()
        elif op == "2": editar_clientes()
        elif op == "3": eliminar_cliente()
        elif op == "4": listar_todo()
        elif op == "5": 
            print("Saliendo del módulo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")