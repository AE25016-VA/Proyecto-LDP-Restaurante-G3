from infraestructura import (
    mostrar_turnos,
    determinar_turno,
    guardar_mesas,
    cargar_mesas,
    reporte_infraestructura
)

print("===== PRUEBA DE TURNOS =====")

# Mostrar turnos
mostrar_turnos()

# Probar determinar_turno
print("\n===== PRUEBA DETERMINAR TURNO =====")

horas = [
    "08:30",
    "13:00",
    "20:15",
    "23:00"
]

for hora in horas:
    resultado = determinar_turno(hora)
    print(f"Hora: {hora} -> Turno: {resultado}")

# Datos de prueba para mesas
mesas_prueba = [
    {
        "numero": 1,
        "capacidad": 4
    },
    {
        "numero": 2,
        "capacidad": 6
    },
    {
        "numero": 3,
        "capacidad": 2
    }
]

print("\n===== PRUEBA GUARDAR MESAS =====")
guardar_mesas(mesas_prueba)

print("\n===== PRUEBA CARGAR MESAS =====")
mesas_cargadas = cargar_mesas()

print("\nMesas cargadas:")
print(mesas_cargadas)

print("\n===== PRUEBA REPORTE =====")
reporte_infraestructura(mesas_cargadas)