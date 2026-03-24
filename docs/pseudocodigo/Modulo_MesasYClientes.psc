Algoritmo Modulo_MesasYClientes
    //Variables CLIENTES
	Definir a, totalClientes Como Entero
	Definir continuarClientes, nombreAux Como Caracter
	Definir nombreRepetido Como Logico
	
	Dimension  nombreClientes[100]
	Dimension telefonoClientes[100]
	totalClientes <- 0
	
	//Variable MESAS
	Definir numeroMesa, capacidad, i, totalMesas Como Entero
    Definir continuarMesas Como Caracter
    Definir esDuplicada Como Logico
    
    Dimension numeroMesas[100]
    Dimension capacidades[100]
    totalMesas <- 0
	
	//Seccion Clientes
	Escribir "Registro de Clientes"
	Repetir
		Escribir "Ingrese nombre del cliente:"
		Leer nombreAux
		
		nombreRepetido <- Falso
		Si totalClientes > 0 Entonces
			Para a <-1 Hasta totalClientes Hacer
				Si Mayusculas(nombreClientes[a]) = Mayusculas(nombreAux) Entonces
					Escribir "ERROR: Este cliente ya está registrado."
					nombreRepetido <- Verdadero
				FinSi
			FinPara
		FinSi
		
		Si nombreRepetido = Falso Entonces
			totalClientes <- totalClientes +1
			nombreClientes[totalClientes] <- nombreAux
			Escribir "Ingrese el numero de teléfono de ", nombreAux, ":"
			Leer telefonoClientes[totalClientes]
			Escribir "Cliente ", nombreAux, " guardado con éxito."
		FinSi
		
		Repetir
			Escribir "¿Desea registrar otro cliente? (Si/No)"
			Leer continuarClientes
			Si Mayusculas(continuarClientes) <> "SI" Y Mayusculas(continuarClientes) <> "NO" Entonces
				Escribir "ERROR: Por favor responda Si o No."
			FinSi
		Hasta Que Mayusculas(continuarClientes) = "SI" O Mayusculas(continuarClientes) = "NO"
	Hasta Que Mayusculas(continuarClientes) = "NO"
	
    //Seccion MESAS
	Escribir ""
    Escribir "Registro de Mesas	"
    
    Repetir
        Escribir "Ingrese el número de la mesa:"
        Leer numeroMesa
        
        esDuplicada <- Falso
        
        Si totalMesas > 0 Entonces
            Para i <- 1 Hasta totalMesas Hacer
                Si numeroMesas[i] = numeroMesa Entonces
                    Escribir "ERROR: La mesa ya está registrada."
                    esDuplicada <- Verdadero
                FinSi
            FinPara
        FinSi
        
        Si esDuplicada = Falso Entonces
            Repetir
                Escribir "Ingrese la capacidad de la mesa:"
                Leer capacidad
                Si capacidad <= 0 Entonces
                    Escribir "ERROR: La capacidad debe ser un número positivo."
                FinSi
            Hasta Que capacidad > 0
            
            totalMesas <- totalMesas + 1
            numeroMesas[totalMesas] <- numeroMesa
            capacidades[totalMesas] <- capacidad
            Escribir "Mesa #", numeroMesa, " registrada exitosamente."
        FinSi
		
		Repetir 
            Escribir "¿Desea registrar otra mesa? (Si/No)"
            Leer continuarMesas
            Si Mayusculas(continuarMesas) <> "SI" Y Mayusculas(continuarMesas) <> "NO" Entonces
                Escribir "ERROR: Por favor responda Si o No."
            FinSi
        Hasta Que Mayusculas(continuarMesas) = "SI" O Mayusculas(continuarMesas) = "NO"
	Hasta Que Mayusculas(continuarMesas) = "NO"
	
    Escribir "RESUMEN FINAL:"
	Escribir "Clientes Registrados:"
	Para a <- 1 Hasta totalClientes Hacer
		Escribir  "Nombre: ", nombreClientes[a], " - teléfono: ", telefonoClientes[a]
	FinPara
    Escribir "Mesas Registradas:"
    Para i <- 1 Hasta totalMesas Hacer
        Escribir "Mesa #", numeroMesas[i], " - Capacidad: ", capacidades[i]
    FinPara
FinAlgoritmo
