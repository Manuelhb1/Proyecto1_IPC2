
from nodo import Nodo

class ListaDobleEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def vacia(self):
        return self.primero == None

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.tamanio += 1
    
    def recorrerInicio(self):
        if self.vacia():
            return "Lista vacia"
            
        aux = self.primero
        while aux:
            print(aux.dato,end="-")
            aux = aux.siguiente 


    def recorrer(self):
        if self.vacia():
            return "Lista vacia"
        aux = self.primero
        print(aux.dato,end = "-")
        while aux.siguiente:
            aux = aux.siguiente
            print(aux.dato, end = "-")            


    #def recorrerFin(self):
    #    aux = self.ultimo
    #    while aux:
    #        print(aux.dato)
    #        aux = aux.anterior

    #---------Busca un dato por su posicion iniciando en 0, por insercion al inicio
    
    def buscarPosicion(self, posicion):
        aux = self.primero        
        posList = 0
        while aux:
            if posicion>(self.tamanio-1):
                return "Error indice fuera de rango" 
                            
            if posList == posicion:
                return aux.dato
            posList += 1
            aux = aux.siguiente
            
        
        