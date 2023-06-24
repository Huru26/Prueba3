import numpy as np
import msvcrt


while True:
    print("")
    print("Numero de Identificacion Fiscal")
    print("")
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir Certificados")
    print("4.- Salir")
    print("")

    opc = int(input("Seleccione opcion: "))
    if opc < 1 or opc > 4: 
        print ()
        print ("ERROR =====> La opcion ingresada es incorrecta, intenta nuevamente")
        print("Presione una tecla para cargar nuevamente el MENU...")
        msvcrt.getch()  
        print ("")
        
    try:

        
        if opc == 1:
                print ("")
                print ("Ingresar datos de la persona.\n")
                nom_pasajero = str(input("Nombre y Apellidos: "))
                nif = str(input("Ingrese numero de NIF (sin puntos y con guion):"))
                edad = int (input("Edad de la persona: "))
                edad >= 0
            
        else:
            if opc == 2:
                print()
                
                     
            else:   

                if opc == 3:
                    print("Nombre: ",nom_pasajero) 
                    print("NIF: ",nif)
                    print("Edad: ",edad)
                    if edad > 15:
                        print("Pertenece a la Union Europea")
                    else:
                        print("No pertenece a la Union Europea")   

                if opc == 4:
                    print("Que tengas excelente prueba") 
                    break
        
    except:
        print ("ERROR =====> Datos incorrecto")



