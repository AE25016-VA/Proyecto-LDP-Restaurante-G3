#Comenzanr el modulo
clientes = []
mesas = []

#Clientes 
def registrar_clientes():
    print("\nREGISTRO DE CLIENTE Y MESA")
    nombre = input("Ingrese nombre del cliente: ")
    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    if any (c['nombre'].upper() == nombre.upper() for c in clientes):
        print("ERROR: Este cliente ya está registrado.")
        return
    
    telefono = input(f"Ingrese el número del teléfono de {nombre}: ")

    try:
        mesa1 = int(input("¿Qué número de mesa desea reservar?: "))
        mesas.append(mesa1) # Guardamos la mesa deseada en la lista mesas del inicio
        
        # Opción por si quiere añadir otra mesa deseada
        resp = input("¿Desea añadir otra mesa deseada? (s/n): ").strip().lower()
        if resp == 's':
            mesa2 = int(input("Ingrese la otra mesa deseada: "))
            mesas.append(mesa2)
            mesas_cliente = [mesa1, mesa2]
        else:
            mesas_cliente = [mesa1]
            
        # Guardamos en la lista de clientes
        clientes.append({
            "nombre": nombre,
            "telefono": telefono,
            "mesas_deseadas": mesas_cliente
        })
        print(f"Pre-registro de {nombre} guardado con éxito con sus mesas deseadas.")
        
    except ValueError:
        print("ERROR: Ingrese un número de mesa válido. Registro cancelado.")

def editar_clientes ():
    nombre_buscar = input("Nombre del cliente a editar: ")
    for cliente in clientes:
        if cliente['nombre'].upper() == nombre_buscar.upper():
           cliente['telefono'] = input("Nuevo teléfono: ")
           print("Datos atualizados.")
           return
    print ("Cliente no encontrado.")

def eliminar_cliente():
    nombre_buscar = input("Nombre del cliente a eliminar: ")
    global clientes
    antes = len(clientes)
    clientes = [c for c in clientes if c['nombre'].upper() != nombre_buscar.upper()]
    if len(clientes) < antes:
        print("Cliente eliminado con éxito.")
    else:
        print("Si el cliente existía, ha sido eliminado.")
                        
def listar_todo():
    print("RESUMEN FINAL")
    print("Clientes:", clientes)
    print("Mesas:", mesas)

#Menu de prueba
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
        elif op == "5": break

