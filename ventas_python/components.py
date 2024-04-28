from utilities import  gotoxy, blue_color
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input(blue_color+f"Elija opcion[1...{len(self.opciones)}]: ") 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True:
            gotoxy(col, fil)
            try:
                valor = input()
                if valor.isdigit:
                    return int(valor)
                else:
                    gotoxy(col, fil);print(mensajeError)
                    time.sleep(1)
                    gotoxy(col, fil);print(' ' * 40)
            except:
                gotoxy(col, fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil);print(' ' * 40)

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print(f'"          ------><  | {mensajeError} "')
        return valor

    def solo_decimales(self, mensajeError, col, fil):
        while True:
            gotoxy(col, fil)
            try:
                valor = float(input())
                if valor > 0:
                    return valor
                else:
                    gotoxy(col, fil);print(mensajeError)
                    time.sleep(1)
                    gotoxy(col, fil);print(' ' * 40)
            except:
                gotoxy(col, fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil);print(' ' * 40)
    
    def cedula(self, mensajeError, col, fil):
        while True:
            gotoxy(col, fil);dni = input()
            if len(dni) == 10 and dni != '9999999999':
                    break
            else:
                gotoxy(col, fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil);print(' '*20)
        return dni


if __name__ == '__main__':
    # instanciar el menu
    valida = Valida()
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)

    cedula = valida.cedula('Ingrese su cédula', "Cédula inválida.")
    print("Cédula validada:", cedula)