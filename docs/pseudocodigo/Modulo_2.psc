Algoritmo Modulo_LogicaReservas
	
	// =============================================
	// MESAS DE EJEMPLO 
	// =============================================
	Definir totalMesas Como Entero
	Dimension numeroMesas[100]
	Dimension capacidades[100]
	
	totalMesas <- 3
	numeroMesas[1] <- 1
	capacidades[1] <- 4
	numeroMesas[2] <- 2
	capacidades[2] <- 8
	numeroMesas[3] <- 3
	capacidades[3] <- 2
	
	// =============================================
	// VARIABLES PARA RESERVAS
	// =============================================
	Definir totalReservas, i, j, indiceM Como Entero
	Definir mesaSolicitada, personasSolicitadas Como Entero
	Definir nombreCliente, fecha, turno, continuar Como Caracter
	Definir mesaEncontrada, superposicion Como Logico

    Dimension indiceMReserva[100]
	Dimension clienteReserva[100]
	Dimension mesaReserva[100]
	Dimension fechaReserva[100]
	Dimension turnoReserva[100]
	Dimension personasReserva[100]
	
	totalReservas <- 0
	
	// =============================================
	// SECCIÓN: CREAR RESERVAS
	// =============================================
	Escribir "=============================="
	Escribir "   MÓDULO DE RESERVAS"
	Escribir "=============================="
	
	Repetir
		Escribir ""
		Escribir "--- Nueva Reserva ---"
		
		// Paso 1: Nombre del cliente
		Escribir "Ingrese el nombre del cliente:"
		Leer nombreCliente
		
		// Paso 2: Número de mesa
		Escribir "Ingrese el número de mesa deseado:"
		Leer mesaSolicitada
		
		// Verificar que la mesa existe
		mesaEncontrada <- Falso
		indiceM <- 0
		Para i <- 1 Hasta totalMesas Hacer
			Si numeroMesas[i] = mesaSolicitada Entonces
				mesaEncontrada <- Verdadero
				indiceM <- i
			FinSi
		FinPara
		
		Si mesaEncontrada = Falso Entonces
			Escribir "ERROR: La mesa #", mesaSolicitada, " no existe en el sistema."
			
		SiNo
			// Paso 3: Número de personas + VALIDACIÓN DE CAPACIDAD
			Repetir
				Escribir "Ingrese el número de personas para la reserva:"
				Leer personasSolicitadas
				Si personasSolicitadas <= 0 Entonces
					Escribir "ERROR: El número de personas debe ser mayor a cero."
				FinSi
			Hasta Que personasSolicitadas > 0
			
			Si personasSolicitadas > capacidades[indiceM] Entonces
				Escribir "ERROR: Capacidad insuficiente."
				Escribir "La mesa #", mesaSolicitada, " tiene capacidad para ", capacidades[indiceM], " personas."
				Escribir "No se pueden acomodar ", personasSolicitadas, " personas en esta mesa."
				
			SiNo
				// Paso 4: Fecha
				Escribir "Ingrese la fecha de la reserva (DD/MM/AAAA):"
				Leer fecha
				
				// Paso 5: Turno + VALIDACIÓN
				Repetir
					Escribir "Ingrese el turno (Mañana / Tarde / Noche):"
					Leer turno
					Si Mayusculas(turno) <> "MAÑANA" Y Mayusculas(turno) <> "TARDE" Y Mayusculas(turno) <> "NOCHE" Entonces
						Escribir "ERROR: Turno inválido. Elija entre Mañana, Tarde o Noche."
					FinSi
				Hasta Que Mayusculas(turno) = "MAÑANA" O Mayusculas(turno) = "TARDE" O Mayusculas(turno) = "NOCHE"
				
				// Paso 6: VALIDACIÓN DE SUPERPOSICIÓN DE HORARIOS
				superposicion <- Falso
				Si totalReservas > 0 Entonces
					Para j <- 1 Hasta totalReservas Hacer
						Si mesaReserva[j] = mesaSolicitada Y fechaReserva[j] = fecha Y Mayusculas(turnoReserva[j]) = Mayusculas(turno) Entonces
							superposicion <- Verdadero
						FinSi
					FinPara
				FinSi
				
				Si superposicion = Verdadero Entonces
					Escribir "ERROR: Superposición de horarios detectada."
					Escribir "La mesa #", mesaSolicitada, " ya tiene una reserva el ", fecha, " en el turno ", turno, "."
					
				SiNo
					// Guardar la reserva
					totalReservas <- totalReservas + 1
					clienteReserva[totalReservas]  <- nombreCliente
					mesaReserva[totalReservas]     <- mesaSolicitada
					indiceMReserva[totalReservas]  <- indiceM  
					fechaReserva[totalReservas]    <- fecha
					turnoReserva[totalReservas]    <- turno
					personasReserva[totalReservas] <- personasSolicitadas
					Escribir "Reserva registrada exitosamente para ", nombreCliente, "."
				FinSi
				
			FinSi
		FinSi
		
		// Preguntar si continúa
		Repetir
			Escribir "¿Desea registrar otra reserva? (Si/No)"
			Leer continuar
			Si Mayusculas(continuar) <> "SI" Y Mayusculas(continuar) <> "NO" Entonces
				Escribir "ERROR: Por favor responda Si o No."
			FinSi
		Hasta Que Mayusculas(continuar) = "SI" O Mayusculas(continuar) = "NO"
		
	Hasta Que Mayusculas(continuar) = "NO"
	
	// =============================================
	// RESUMEN FINAL DE RESERVAS
	// =============================================
	Escribir ""
	Escribir "=============================="
	Escribir "   RESUMEN DE RESERVAS"
	Escribir "=============================="
	
	Si totalReservas = 0 Entonces
		Escribir "No se registró ninguna reserva."
	SiNo
Para i <- 1 Hasta totalReservas Hacer
    Escribir "Reserva #", i
    Escribir "  Cliente   : ", clienteReserva[i]
    Escribir "  Mesa      : #", mesaReserva[i], " (Capacidad: ", capacidades[indiceMReserva[i]], " personas)"
    Escribir "  Turno ID  : ", turnoReserva[i]
    Escribir "  Fecha     : ", fechaReserva[i]
    Escribir "  Personas  : ", personasReserva[i]
FinPara
	FinSi

FinAlgoritmo
