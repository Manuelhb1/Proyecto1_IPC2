import os
import time
from listaDobleEnlazada import ListaDobleEnlazada
from datos import Piso
from xml.dom import minidom
import xml.etree.ElementTree as ET
from patron import Patron

class ManejoArchivo:

    def limpiar(self):
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")


    def manejoXML(self):
        
        
        listaPisos = ListaDobleEnlazada()    #Lista que guarda los pisos
        listaPatrones = ListaDobleEnlazada()  #Lista auxiliar para guardar los patrones
                    
        tree = ET.parse('prueva.xml')
        raiz = tree.getroot()
        
        for i in raiz:      

            for j in i.findall('./patrones/patron'):
                nuevoPatron = Patron(j.text,j.attrib["codigo"])
                listaPatrones.agregarFinal(nuevoPatron)      
                      
            nuevopiso = Piso(i.attrib["nombre"], int(i.findtext('R')), int(i.findtext('C')),i.findtext('F') ,int(i.findtext('S')),listaPatrones)                            
            listaPisos.agregarFinal(nuevopiso)



        for i in range(listaPisos.tamanio):
            print(listaPisos.buscarPosicion(i).patrones.buscarPosicion(0).nombre)
        
        


           
mn = ManejoArchivo()
mn.manejoXML()
#mn.limpiar()        
    
    


