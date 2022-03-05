from manejoArchivo import ManejoArchivo



class Main:    
    def inicio():

        ar1 = ManejoArchivo()

        salirMenu = True

        print("\n\n")
        print("""        +---------------------------------+
        |  Menu:                          |
        |                                 |
        |  1 Cargar xml                   |
        |  2 Mostrar pisos cargados       |
        |  3 Seleccionar piso             |        
        |  4 Salir                        | 
        +---------------------------------+
        
        """)
        
        
        while salirMenu:
        
            entrada = int(input("Ingresa una opcion:  " ))
            print("")
        
            if entrada == 1:
                ar1.manejoXML()
                if ar1.manejoXML():
                    print("\n\nArchivo xml cargado correctamente\n\n")
        
            elif entrada ==2:
                ar1.mostrarPisos()
        
            elif entrada == "3":
                print("falta")
            
            elif entrada == "4":
                print("Saliendo...")
                print("\n\n\n")
                salirMenu = False
                exit()
            entrada = 0
    inicio()