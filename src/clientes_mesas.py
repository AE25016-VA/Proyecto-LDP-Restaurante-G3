#Comenzanr el modulo
    try:
        numero = int(input("Ingrese el número de la mesa: "))
        if any (m['numero'] == numero for m in mesas):
            print("ERROR: La mesa ya está registrada.")
            return
        
        capacidad = 0
        while capacidad <= 0:
            capacidad = int(input("Ingrese la capacidad de la mesa: "))
            if capacidad <= 0:
                print("ERROR: La capacidad debe ser un número positivo.")

        mesas.append({"numero": numero, "capacidad": capacidad})
        print(f"Mesa #{numero} registrada exitosamente.")
    except ValueError:
        print("ERROR: Ingrese un número válido.")

def editar_mesa():
    try:
        num_buscar = int(input("Número de la mesa a editar: "))
        for mesa in mesas:
            if mesa['numero'] == num_buscar:
                mesa['capacidad'] = int(input("Nueva capacidad: "))
        print("Mesa no encontrada.")
    except ValueError:
        print("ERROR: Ingrese valores numéricos.")

def eliminar_mesa():
    try:
        num_buscar = int(input("Número de mesa a eliminar: ")) 
        global mesas
        mesas = [m for m in mesas if m['numero'] != num_buscar]
        print("Si la mesa existía, ha sido eliminada.")
    except ValueError:
        print("ERROR: Ingrse un número válido.")
                        

def listar_todo():
    print("RESUMEN FINAL")
    print("Clientes:", clientes)
    print("Mesas:", mesas)

#Menu de prueba
def menu_modulo1():
    while True:
        print(" ")
        print("MODULO CLIENTES Y MESAS")  
        print("1. Registrar Cliente")
        print("2. Editar Cliente")
        print("3. Eliminar Cliente")
        print("4. Registrar Mesa")
        print("5. Editar Mesa")
        print("6. Eliminar Mesa")
        print("7. Ver todo")
        print("8. Salir")
        op = input("Seleccione una opción: ")
        print(" ")

        if op == "1": registrar_clientes()
        elif op == "2": editar_clientes()
        elif op == "3": eliminar_cliente()
        elif op == "4": registrar_mesa()
        elif op == "5": editar_mesa()
        elif op == "6": eliminar_mesa()
        elif op == "7": listar_todo()
        elif op == "8": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu_modulo1()
