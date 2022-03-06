from manejoArchivo import ManejoArchivo



class Main:    
    def inicio():

        ar1 = ManejoArchivo()

        salirMenu = True
        entradaPiso = True

        print("\n")
        print(f"{'':<5}{'+---------------------------------+':<30}\n{'':<5}{'|':<4}{'Menu':<30}|\n{'':<5}{'|':<4}{'':<30}|\n{'':<5}{'|':<4}{'1 Cargar xml':<30}|\n{'':<5}{'|':<4}{'2 Mostrar pisos cargados':<30}|\n{'':<5}{'|':<4}{'3 Seleccionar piso':<30}|\n{'':<5}{'|':<4}{'4 Salir':<30}|\n{'':<5}{'+---------------------------------+':<30}\n")                  
        
        while salirMenu:            
        
            entrada = int(input("Ingresa una opcion:  " ))
            print("")
        
            if entrada == 1:
                ar1.__manejoXML__()
                if ar1.getPisos():
                    print("\nArchivo xml cargado correctamente\n\n")
                            
            elif entrada == 2:
                #Aun no esta en orden albabetico
                ar1.mostrarPisos()                
        
            elif entrada == 3:                
                npiso = int(input(f"{'Ingresa el piso que desees: ':<10}"))
                ar1.seleccionarPiso(npiso)
                print(f"\n{'':<15}1. Seleccionar un patron\n{'':<15}2. Cambiar patron\n{'':<15}3. Regresar\n\n")  
                              
                while entradaPiso == True:
                    
                    entOp = int(input("Ingresa una opcion"))
                    if entOp == 1:
                        posp = int(input(f"{'Ingresa el patron que desees: ':<10}"))
                        ar1.seleccionarPatron(posp)
                        ar1.mostrarConGraphviz()

                        
                    if entOp ==2:
                        print("falta")
                    if entOp == 3:
                        print("\n")

                        print(f"{'':<5}{'+---------------------------------+':<30}\n{'':<5}{'|':<4}{'Menu':<30}|\n{'':<5}{'|':<4}{'':<30}|\n{'':<5}{'|':<4}{'1 Cargar xml':<30}|\n{'':<5}{'|':<4}{'2 Mostrar pisos cargados':<30}|\n{'':<5}{'|':<4}{'3 Seleccionar piso':<30}|\n{'':<5}{'|':<4}{'4 Salir':<30}|\n{'':<5}{'+---------------------------------+':<30}\n")                  
                        break
                       
            elif entrada == 4:
                print("Saliendo...")
                print("\n\n\n")
                salirMenu = False
                exit()
            entrada = 0
    inicio()