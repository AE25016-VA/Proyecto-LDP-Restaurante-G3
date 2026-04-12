Proceso Modulo_Infraestructura
	
    // VARIABLES TURNOS
    Definir i, totalTurnos Como Entero
    Definir turno_id Como Entero
    Definir turno_nombre, turno_inicio, turno_fin Como Cadena
	
    Dimension turno_id[10]
    Dimension turno_nombre[10]
    Dimension turno_inicio[10]
    Dimension turno_fin[10]
	
    totalTurnos <- 3
	
    turno_id[1] <- 1
    turno_nombre[1] <- "Desayuno"
    turno_inicio[1] <- "07:00"
    turno_fin[1]    <- "10:00"
	
    turno_id[2] <- 2
    turno_nombre[2] <- "Almuerzo"
    turno_inicio[2] <- "12:00"
    turno_fin[2]    <- "15:00"
	
    turno_id[3] <- 3
    turno_nombre[3] <- "Cena"
    turno_inicio[3] <- "19:00"
    turno_fin[3]    <- "22:00"
	
    mostrarTurnos(turno_id, turno_nombre, turno_inicio, turno_fin, totalTurnos)
	
FinProceso
SubProceso mostrarTurnos(turno_id, turno_nombre, turno_inicio, turno_fin, totalTurnos)
    Definir i Como Entero
    Escribir "Turnos disponibles:"
    Para i <- 1 Hasta totalTurnos Hacer
        Escribir turno_id[i], " - ", turno_nombre[i], " -> ", turno_inicio[i], " a ", turno_fin[i]
    FinPara
FinSubProceso
SubProceso guardarClientes(nombreClientes, telefonoClientes, totalClientes)
    Definir i Como Entero
    Escribir "-- Guardando clientes --"
    Para i <- 1 Hasta totalClientes Hacer
        Escribir nombreClientes[i], ",", telefonoClientes[i]
    FinPara
    Escribir "Clientes guardados correctamente."
FinSubProceso
SubProceso cargarClientes(nombreClientes, telefonoClientes, totalClientes)
    Escribir "-- Cargando clientes --"
    Escribir "Clientes cargados correctamente."
FinSubProceso
SubProceso guardarMesas(numeroMesas, capacidades, totalMesas)
    Definir i Como Entero
    Escribir "-- Guardando mesas --"
    Para i <- 1 Hasta totalMesas Hacer
        Escribir numeroMesas[i], ",", capacidades[i]
    FinPara
    Escribir "Mesas guardadas correctamente."
FinSubProceso
SubProceso cargarMesas(numeroMesas, capacidades, totalMesas)
    Escribir "-- Cargando mesas --"
    Escribir "Mesas cargadas correctamente."
FinSubProceso
SubProceso guardarReservas(reservasCliente, reservasMesa, reservasTurno, reservasFecha, totalReservas)
    Definir i Como Entero
    Escribir "-- Guardando reservas --"
    Para i <- 1 Hasta totalReservas Hacer
        Escribir reservasCliente[i], ",", reservasMesa[i], ",", reservasTurno[i], ",", reservasFecha[i]
    FinPara
    Escribir "Reservas guardadas correctamente."
FinSubProceso
SubProceso cargarReservas(reservasCliente, reservasMesa, reservasTurno, reservasFecha, totalReservas)
    Escribir "-- Cargando reservas --"
    Escribir "Reservas cargadas correctamente."
FinSubProceso