import json
import os

# TURNOS DEL RESTAURANTE

turnos = [
    {
        "nombre": "Desayuno",
        "inicio": "07:00",
        "fin": "10:00"
    },
    {
        "nombre": "Almuerzo",
        "inicio": "12:00",
        "fin": "15:00"
    },
    {
        "nombre": "Cena",
        "inicio": "19:00",
        "fin": "22:00"
    }
]

                                         
# MOSTRAR TURNOS

def mostrar_turnos():

    print("\n===== TURNOS DISPONIBLES =====")

    for turno in turnos:

        print(
            f"{turno['nombre']} "
            f"({turno['inicio']} - {turno['fin']})"
        )


# DETERMINAR TURNO

def determinar_turno(hora_ingresada):

    try:

        for turno in turnos:

            if (
                hora_ingresada >= turno['inicio']
                and
                hora_ingresada < turno['fin']
            ):

                return turno['nombre']

        return None

    except:
        return None

# PERSISTENCIA DE MESAS

def guardar_mesas(mesas):

    try:

        with open(
            "mesas.json",
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                mesas,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("Mesas guardadas correctamente.")

    except Exception as e:

        print("ERROR al guardar mesas:", e)


def cargar_mesas():

    try:

        if os.path.exists("mesas.json"):

            with open(
                "mesas.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                mesas = json.load(archivo)

            print("Mesas cargadas correctamente.")
            return mesas

        return []

    except Exception as e:

        print("ERROR al cargar mesas:", e)
        return []


# REPORTE INFRAESTRUCTURA

def reporte_infraestructura(mesas):

    print("\n===== REPORTE INFRAESTRUCTURA =====")

    print("\nTURNOS:")

    for turno in turnos:

        print(
            f"- {turno['nombre']}: "
            f"{turno['inicio']} a {turno['fin']}"
        )

    print("\nMESAS:")

    if len(mesas) == 0:

        print("No hay mesas registradas.")

    else:

        for mesa in mesas:

            print(
                f"Mesa #{mesa['numero']} "
                f"| Capacidad: {mesa['capacidad']}"
            )

    print(f"\nTotal de mesas: {len(mesas)}")