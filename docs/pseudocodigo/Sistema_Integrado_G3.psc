Algoritmo Sistema_Integrado_G3
    // VARIABLES GLOBALES (UNIFICADAS)
    
    // Variables Persona 1 (Vanessa AE25016): Mesas y Clientes
    Definir totalClientes, totalMesas, a, i, capacidad, numeroMesa Como Entero
    Definir continuarClientes, continuarMesas, nombreAux Como Caracter
    Definir nombreRepetido, esDuplicada Como Logico
    Dimension nombreClientes[100], telefonoClientes[100], numeroMesas[100], capacidades[100]
    totalClientes <- 0
    totalMesas <- 0
    
    // Variables Persona 2 (Enoc CV19058): Reservas
    Definir totalReservas, j, indiceM, mesaSolicitada, personasSolicitadas Como Entero
    Definir nombreCReserva, fecha, turno, continuarRes, horaIngresada Como Caracter
    Definir mesaEncontrada, superposicion Como Logico
    Dimension clienteReserva[100], mesaReserva[100], fechaReserva[100], turnoReserva[100], personasReserva[100], indiceMReserva[100]
    totalReservas <- 0
    
    // Variables Persona 3 (Rafael CA25045): Turnos
    Definir totalTurnos Como Entero
    Definir t_nombre, t_inicio, t_fin Como Cadena
    Dimension t_nombre[10], t_inicio[10], t_fin[10]
    
    totalTurnos <- 3
    t_nombre[1] <- "Desayuno"; t_inicio[1] <- "07:00"; t_fin[1] <- "10:00"
    t_nombre[2] <- "Almuerzo"; t_inicio[2] <- "12:00"; t_fin[2] <- "15:00"
    t_nombre[3] <- "Cena";     t_inicio[3] <- "19:00"; t_fin[3] <- "22:00"
    
    Definir opcion Como Entero
    
    Repetir
        Limpiar Pantalla
        Escribir "SISTEMA DE RESERVAS PARA EL RESTAURANTE - GRUPO 3"
        Escribir "(1) Registro de Clientes y Mesas (Vanessa)"
        Escribir "(2) Gestión de Reservas (Enoc)"
        Escribir "(3) Ver Turnos e Infraestructura (Rafael)"
        Escribir "(4) Resumen General del Sistema"
        Escribir "(5) Salir"
        Leer opcion
        
        Segun opcion Hacer
            1:
                Escribir "--- Registro de Clientes ---"
                Repetir
                    Escribir "Ingrese nombre del cliente:"
                    Leer nombreAux
                    nombreRepetido <- Falso
                    Si totalClientes > 0 Entonces
                        Para a <- 1 Hasta totalClientes Hacer
                            Si Mayusculas(nombreClientes[a]) = Mayusculas(nombreAux) Entonces
                                Escribir "ERROR: Cliente ya registrado."
                                nombreRepetido <- Verdadero
                            FinSi
                        FinPara
                    FinSi
                    Si nombreRepetido = Falso Entonces
                        totalClientes <- totalClientes + 1
                        nombreClientes[totalClientes] <- nombreAux
                        Escribir "Teléfono de ", nombreAux, ":"
                        Leer telefonoClientes[totalClientes]
                    FinSi
                    Repetir
                        Escribir "¿Otro cliente? (Si/No)"
                        Leer continuarClientes
                    Hasta Que Mayusculas(continuarClientes) = "SI" O Mayusculas(continuarClientes) = "NO"
                Hasta Que Mayusculas(continuarClientes) = "NO"
                
                Escribir "--- Registro de Mesas ---"
                Repetir
                    Escribir "Número de la mesa:"
                    Leer numeroMesa
                    esDuplicada <- Falso
                    Si totalMesas > 0 Entonces
                        Para i <- 1 Hasta totalMesas Hacer
                            Si numeroMesas[i] = numeroMesa Entonces
                                Escribir "ERROR: Mesa ya registrada."
                                esDuplicada <- Verdadero
                            FinSi
                        FinPara
                    FinSi
                    Si esDuplicada = Falso Entonces
                        Repetir
                            Escribir "Capacidad:"
                            Leer capacidad
                        Hasta Que capacidad > 0
                        totalMesas <- totalMesas + 1
                        numeroMesas[totalMesas] <- numeroMesa
                        capacidades[totalMesas] <- capacidad
                    FinSi
                    Repetir
                        Escribir "¿Otra mesa? (Si/No)"
                        Leer continuarMesas
                    Hasta Que Mayusculas(continuarMesas) = "SI" O Mayusculas(continuarMesas) = "NO"
                Hasta Que Mayusculas(continuarMesas) = "NO"
                
            2:
                Si totalMesas = 0 Entonces
                    Escribir "ERROR: Debe registrar mesas primero en el Módulo 1."
                SiNo
                    Escribir "--- Nueva Reserva ---"
                    Escribir "Nombre del cliente quien realizo la reserva:"
                    Leer nombreCReserva
                    
                    Escribir "Número de mesa reservada:"
                    Leer mesaSolicitada
                    
                    mesaEncontrada <- Falso
                    indiceM <- 0
                    Para i <- 1 Hasta totalMesas Hacer
                        Si numeroMesas[i] = mesaSolicitada Entonces
                            mesaEncontrada <- Verdadero
                            indiceM <- i
                        FinSi
                    FinPara
                    
                    Si mesaEncontrada = Falso Entonces
                        Escribir "ERROR: La mesa #", mesaSolicitada, " no existe."
                    SiNo
                        Escribir "La mesa #", mesaSolicitada, " tiene capacidad para ", capacidades[indiceM], " personas."
                        
                        Escribir "Fecha (DD/MM/AAAA):"
                        Leer fecha
                        
                        Escribir "Turnos disponibles:"
                        Para i <- 1 Hasta totalTurnos Hacer
                            Escribir "  ", t_nombre[i], ": ", t_inicio[i], " a ", t_fin[i]
                        FinPara
                        
                        Escribir "Ingrese la hora de la reserva (formato HH:MM, ej: 14:30):"
                        Leer horaIngresada
                        
                        turno <- ""
                        Para i <- 1 Hasta totalTurnos Hacer
                            Si horaIngresada >= t_inicio[i] Y horaIngresada <= t_fin[i] Entonces
                                turno <- t_nombre[i]
                            FinSi
                        FinPara
                        
                        Si turno = "" Entonces
                            Escribir "ERROR: La hora ", horaIngresada, " no corresponde a ningún turno disponible."
                            Escribir "Los turnos son:"
                            Para i <- 1 Hasta totalTurnos Hacer
                                Escribir "  ", t_nombre[i], ": ", t_inicio[i], " a ", t_fin[i]
                            FinPara
                        SiNo
                            Escribir "Hora ", horaIngresada, " corresponde al turno: ", turno
                            
                            superposicion <- Falso
                            Si totalReservas > 0 Entonces
                                Para j <- 1 Hasta totalReservas Hacer
                                    Si mesaReserva[j] = mesaSolicitada Y fechaReserva[j] = fecha Y Mayusculas(turnoReserva[j]) = Mayusculas(turno) Entonces
                                        superposicion <- Verdadero
                                    FinSi
                                FinPara
                            FinSi
                            
                            Si superposicion Entonces
                                Escribir "ERROR: Esta mesa ya está reservada para ese día y turno."
                            SiNo
                                totalReservas <- totalReservas + 1
                                clienteReserva[totalReservas] <- nombreCReserva
                                mesaReserva[totalReservas] <- mesaSolicitada
                                indiceMReserva[totalReservas] <- indiceM
                                fechaReserva[totalReservas] <- fecha
                                turnoReserva[totalReservas] <- turno
                                personasReserva[totalReservas] <- personasSolicitadas
                                Escribir "¡Reserva registrada con éxito!"
                            FinSi
                        FinSi
                    FinSi
                FinSi
                Escribir "Presione una tecla para volver..."
                Esperar Tecla
                
            3:
                mostrarTurnos(t_nombre, t_inicio, t_fin, totalTurnos)
                Esperar Tecla
                
            4:
                Escribir "--- Reporte de Reservas ---"
                Si totalReservas = 0 Entonces
                    Escribir "No hay reservas registradas."
                SiNo
                    Para i <- 1 Hasta totalReservas Hacer
                        Escribir "Reserva #", i, ": ", clienteReserva[i], " | Mesa: #", mesaReserva[i], " (Cap: ", capacidades[indiceMReserva[i]], ") | Turno: ", turnoReserva[i], " | Fecha: ", fechaReserva[i]
                    FinPara
                FinSi
                Escribir "Presione una tecla para volver..."
                Esperar Tecla
                
            5:
                Escribir "Saliendo del sistema..."
        FinSegun
    Hasta Que opcion = 5
FinAlgoritmo

SubProceso mostrarTurnos(turno_nombre, turno_inicio, turno_fin, totalTurnos)
    Definir i Como Entero
    Escribir "Turnos disponibles:"
    Para i <- 1 Hasta totalTurnos Hacer
        Escribir turno_nombre[i], " -> ", turno_inicio[i], " a ", turno_fin[i]
    FinPara
FinSubProceso