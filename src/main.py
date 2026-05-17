from clientes_mesas import menu_modulo1, clientes, mesas
from LogicaReservas import menu_modulo2, reservas
from infraestructura import mostrar_turnos, reporte_infraestructura

def menu_principal():
    while True:
        print("\nSISTEMA DE RESTAURANTE")
        print("1. Modulo 1: Clientes y Mesas")
        print("2. Modulo 2: Reservas")
        print("3. Modulo 3: Turnos e Reportes")
        print("4. Ver Reporte General del Sistema")
        print("5. Salir")

        opcion = input("Seleccione una opcion (1-5): ")
        if opcion == "1":
            menu_modulo1()
        elif opcion == "2":
            menu_modulo2()
        elif opcion == "3":
            print("\n1. Mostrar turnos")
            print("2. Regresar")
            sub_opcion = input("Seleccione: ")
            if sub_opcion == "1":
                mostrar_turnos()
        elif opcion == "4":
            print("REPORTES INTEGRADOS")
            print(f"Total de Clientes Registrados: {len(clientes)}")
            print(f"Total de Reservas Formalizadas: {len(reservas)}")
            
            print("\n--- DETALLE DE MESAS SOLICITADAS (Módulo 1) ---")
            if len(mesas) == 0:
                print("No hay preferencias de mesas registradas aún.")
            else:
                # Como tu lista 'mesas' guarda números directamente, los listamos así:
                print("Números de mesas que los clientes desean:", mesas)
            
            print("\n--- DETALLE DE RESERVAS ACTIVAS (Módulo 2) ---")
            if len(reservas) == 0:
                print("No hay reservas confirmadas en el sistema.")
            else:
                # Mostramos de forma compacta e integrada lo que procesó Enoc
                for idx, res in enumerate(reservas, 1):
                    print(f" {idx}. Cliente: {res['cliente']} | Mesa: #{res['numero_mesa']} | Capacidad: {res['capacidad']} pers. | Turno: {res['turno']} ({res['hora']})")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("EROR: opicion no valida. Trate nuevamente.")

if __name__ == "__main__":
    menu_principal()
