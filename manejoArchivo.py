import os
import time

from matplotlib import style
from listaDobleEnlazada import ListaDobleEnlazada
from datos import Piso
from xml.dom import minidom
import xml.etree.ElementTree as ET
from patron import Patron
from graphviz import Digraph




class ManejoArchivo:

    #Lista de los pisos cargados
    def setPisos(self, lpisos):
        self.lpisos =  lpisos

    #Retorna la lista de los pisos cargados
    def getPisos(self):
        return self.lpisos

    #Retorna la posicion del piso que se selecciono//mejor retornar el piso
    def getPisoActual(self):
        return self.retornarPisoActual

    #Retorna la posicion del patron inicial//probando a retornar el patron actual
    def getPosActualPatron(self):
        return self.patronActual    
    
    def __manejoXML__(self):        
        
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
        
        self.setPisos(listaPisos)
        #No retorna nada 


    def mostrarPisos(self): 

        #Se debe mostrar en orden alfabetico

        for y in range(self.getPisos().tamanio):
            print(f"{y+1:<4}{'Nombre':<20}{self.getPisos().buscarPosicion(y).nombre}\n{'':<4}{'Filas':<20}{self.getPisos().buscarPosicion(y).fila}\n{'':4}{'Columnas':<20}{self.getPisos().buscarPosicion(y).columna}\n{'':<4}{'Precio voltear':<20}{self.getPisos().buscarPosicion(y).voltear}\n{'':<4}{'Precio Cambiar':<20}{self.getPisos().buscarPosicion(y).cambiar}")
            
            for x in range(self.getPisos().buscarPosicion(y).patrones.tamanio):
                print(self.getPisos().buscarPosicion(y).patrones.buscarPosicion(x).codigo)
                print(self.getPisos().buscarPosicion(y).patrones.buscarPosicion(x).patron.recorrerInicio())
            print("\n")       
        
    def mostrarPisoPorFilaColumna(self,fila, columna):
        print("hola")
    
    def seleccionarPiso(self, pos):

        print(f"{pos:<4}{'Nombre':<20}{self.getPisos().buscarPosicion(pos-1).nombre}\n{'':<4}{'Filas':<20}{self.getPisos().buscarPosicion(pos-1).fila}\n{'':4}{'Columnas':<20}{self.getPisos().buscarPosicion(pos-1).columna}\n{'':<4}{'Precio voltear':<20}{self.getPisos().buscarPosicion(pos-1).voltear}\n{'':<4}{'Precio Cambiar':<20}{self.getPisos().buscarPosicion(pos-1).cambiar}")
            
        for x in range(self.getPisos().buscarPosicion(pos-1).patrones.tamanio):
            print(self.getPisos().buscarPosicion(pos-1).patrones.buscarPosicion(x).codigo)
            print(self.getPisos().buscarPosicion(pos-1).patrones.buscarPosicion(x).patron.recorrerInicio())
        print("\n")
        
        #guarda el piso actual seleccionado
        self.retornarPisoActual = self.getPisos().buscarPosicion(pos-1)

        #self.posActual = pos
    
    def seleccionarPatron(self, pos):

        print(self.getPisoActual().patrones.buscarPosicion(pos-1).codigo)
        print(self.getPisoActual().patrones.buscarPosicion(pos-1).patron.recorrerInicio())

        #guarda el patron actual
        self.patronActual = self.getPisoActual().patrones.buscarPosicion(pos-1).patron
    

    def mostrarConGraphviz(self):

        dot = Digraph(comment = 'Mostrando patron', node_attr = {"shape": "box", "style": "filled","fontcolor":"black", "fillcolor":"white", "layout":"osage", "style":"invis"}, graph_attr = {"layout":"osage"})
        nodo =""
        cont = 0
        for i in range(self.getPosActualPatron().tamanio):
            
            nodo = "nodo" + str(cont)
          
            if self.getPosActualPatron().buscarPosicion(i) == "B":
                dot.node(nodo, self.getPosActualPatron().buscarPosicion(i), fontcolor="white", color="black", fillcolor = "black")
                
            else:
                dot.node(nodo, self.getPosActualPatron().buscarPosicion(i))

            cont += 1

        dot.render('carpetaSalida/grafica.gv',format='jpg', view=True) 

        print(dot.source)

       
           
#mn = ManejoArchivo()
#mn.__manejoXML__()
#mn.mostrarPisos()
#mn.mostrarConGraphviz()
#mn.inicio()
    
    


