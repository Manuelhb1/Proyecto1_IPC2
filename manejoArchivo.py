import os
import time
from listaDobleEnlazada import ListaDobleEnlazada
from datos import Piso
from xml.dom import minidom
import xml.etree.ElementTree as ET
from patron import Patron

class ManejoArchivo:

     
    def manejoXML(self):        
        
        listaPisos = ListaDobleEnlazada()             
        
        tree = ET.parse('prueva.xml')
        raiz = tree.getroot()
        
        for i in raiz:   

            listaPatrones = ListaDobleEnlazada()             
            for j in i.findall('./patrones/patron'):                

                patron = ListaDobleEnlazada()
                pat = j.text.strip()
                for  k in pat:                                                                                                          
                    patron.agregarFinal(k)
               
                nuevoPatron = Patron(j.attrib["codigo"], patron)
                listaPatrones.agregarFinal(nuevoPatron)                      
                      
            nuevopiso = Piso(i.attrib["nombre"], int(i.findtext('R')), int(i.findtext('C')),int(i.findtext('F')) ,int(i.findtext('S')), listaPatrones)                            
            listaPisos.agregarFinal(nuevopiso)
        
       
        return listaPisos


    def mostrarPisos(self): 

        listapisos = self.manejoXML()

        for y in range(listapisos.tamanio):
            print(f"Nombre: {listapisos.buscarPosicion(y).nombre}\nFilas: {listapisos.buscarPosicion(y).fila}\nColumnas {listapisos.buscarPosicion(y).columna}\nPrecio voltear: {listapisos.buscarPosicion(y).voltear}\nPrecio Cambiar: {listapisos.buscarPosicion(y).cambiar}")
            
            for x in range(listapisos.buscarPosicion(y).patrones.tamanio):
                print(listapisos.buscarPosicion(y).patrones.buscarPosicion(x).codigo)
                print(listapisos.buscarPosicion(y).patrones.buscarPosicion(x).patron.recorrerInicio())
            print("\n")       
        
    

            
           
mn = ManejoArchivo()
mn.mostrarPisos()
#mn.inicio()
    
    


