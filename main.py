import string
import sys
import tkinter as tk
from tkinter import ttk
import pandas as pd

A_Z = list(string.ascii_uppercase)
a_z = list(string.ascii_lowercase)
O_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

gramatica = {
    'S' : ['Url', 'Ruta'],
    'Url' : 'Protocolo // Dominio Puerto / Ruta Parametros Etiquetas',
    'Protocolo' : ['http:', 'https:', 'ftp:', 'mailto:'],
    'Dominio' : 'Sd N . X E',
    'Sd' : ['Palabra .', 'epsilon'],
    'N' : ['Palabra N', 'Num N'],
    'E' : ['. X', 'epsilon'],
    'X' : ['com', 'org', 'info', 'net', 'biz', 'tv', 'cc', 
        'xxx', 'ws', 'aero', 'coop', 'asia', 'mx', 'fr', 
        'us', 'es', 'ar', 'ec', 'eu', 'co', 'bo', 
        'edu'],
    'Puerto' : [': Num', 'epsilon'],
    'Ruta' : ['Rlet Ruta', 'Rnum Ruta', '_ Ruta', '- Ruta', '/Ruta', '.Palabra', 'epsilon'],
    'Parametros' : ['? Palabra P', 'epsilon'],
    'P' : ['Rlet P', 'Rnum P', '= P', '+ P', '& P', '% P', 'epsilon'],
    'Etiquetas' : ['# Palabra E', 'epsilon'],
    'E' : ['Rlet E', 'Rnum E', '= E', '- E', '_ E', '. E', 'epsilon'],
    
    'Ruta' : 'Lunidad \ Carpeta Archivo',
    'Carpeta' : ['Palabra Carpeta', 'Numero Carpeta', '\ '],
    'Archivo' : ['Palabra Archivo', 'Numero Archivo', '. Palabra'],

    'Palabra' : 'Let Rlet',
    'Rlet' : ['Let Rlet', 'epsilon'],
    'Let' : [a_z, A_Z],
    'Num' : 'Dig Rdig',
    'Rdig' : ['Dig Rdig', 'epsilon'],
    'Dig' : [O_9]
}

simboloInicial = 'S'
simbolosTerminales = [[a_z, A_Z], [O_9], '\ ', ':',
        'http:', 'https:', 'ftp:', 'mailto:', 
        'com', 'org', 'info', 'net', 'biz', 'tv', 'cc', 
        'xxx', 'ws', 'aero', 'coop', 'asia', 'mx', 'fr', 
        'us', 'es', 'ar', 'ec', 'eu', 'co', 'bo', 
        'edu']

simbolosNoTerminales = ['S', 'Url', 'Protocolo', 'Dominio', 'Sd', 'N', 'E', 'X', 'Puerto', 'Ruta', 'Parametros', 
                        'P', 'Etiquetas', 'E', 'R', 'Lunidad', 'Carpeta', 'Archivo', 'Palabra', 'Rlet', 'Let',
                        'Num', 'Rdig', 'Dig']

tokens = {
    'Letra_Unidad' : [A_Z],
    'Protocolo' : ['http', 'https', 'ftp', 'mailto'],
    'Extension' : ['com', 'org', 'info', 'net', 'biz', 'tv', 'cc', 
                    'xxx', 'ws', 'aero', 'coop', 'asia', 'mx', 'fr', 
                    'us', 'es', 'ar', 'ec', 'eu', 'co', 'bo', 
                    'edu'],
    'Caracter_Especial' : ['?', '=', '$', '%', '#', '&', '-', '_', '@'],
    'Signos_de_puntuacion' : [':', '.'],
    'Barra' : '/',
    'Barra_inversa' : '\ ',
    'Numero' : [O_9],
    'Letra' : [a_z, A_Z]
}

def AnalisisLexico(Cadena):
    for i in tv1.get_children():
        tv1.delete(i)
    ventana.update()
    token = []
    for i in tokens: 
        print()
        print("Cadena:", Cadena)
        print("token a analisar: ", i)
        lexema = tokens[i]
        print(lexema)
        for j in lexema:
            
            if type(j) == list: #solo entra numero, letra y Unidad
                
                for x in j:
                    if Cadena.find(x) == 0 :
                        print("se encontro una Unidad", x)
                        token.append(str(i) + " : " + str(x))
                        b = list(Cadena)
                        del b[0]
                        Cadena = "".join(b)

                    else:
                        if i != 'Letra_Unidad':
                            existe = Cadena.count(x)
                            if existe > 0:
                                #print(i, " : ", x) 
                                token.append(str(i) + " : " + str(x))
            else: 
                if i == 'Protocolo':
                    x = j + ':'
                    if Cadena.find(x) == 0 :
                        Cadena2 = Cadena[0:6].replace(j, '')
                        token.append(str(i) + " : " + str(j))
                        Cadena = Cadena.replace(Cadena[0:6], Cadena2)
                elif i == 'Extension':
                    aux = '.' + j + '/'
                    posicion = Cadena.find(aux)
                    if posicion >= 0:
                        posicion = posicion + 1
                        token.append(str(i) + " : " + str(j))
                        b = list(Cadena)
                        for c in j:
                            del b[posicion]
                        Cadena = "".join(b)
                    else:
                        aux = '.' + j + '.'
                        posicion = Cadena.find(aux)
                        if posicion >= 0:
                            posicion = posicion + 1
                            b = list(Cadena)
                            token.append(str(i) + " : " + str(j))
                            for c in j:
                                del b[posicion]
                            Cadena = "".join(b)
                else:
                    
                    existe = Cadena.count(j)
                    if existe > 0:
                    #print(i, " : ", j)
                        token.append(str(i) + " : " + str(j))
                        
    
    
    #print(token)
    df = pd.DataFrame()
    df['Token'] = None
    df['Lexema'] = None
    for i in range(len(token)):
        entrada = token[i].split()
        nueva_fila = { 'Token': entrada[0], 'Lexema': entrada[2]} # creamos un diccionario
        df = df.append(nueva_fila, ignore_index=True)
    
    


    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    datos_rows = df.to_numpy().tolist()
    for row in datos_rows:
        tv1.insert("", "end", values=row)

    return df

def AnalisisSintactico(cadena):
    S_inicial(cadena)
    


def S_inicial(cadena):
    print("--> entro al metodo S_inicial")

    if cadena.find('\\') >= 0:
        print("Es una ruta :)")
        R(cadena)
        

    elif cadena.find('/') >= 0:
        print("Es una URL :)")
        U(cadena)
    
    else:
        print("cadena incorrecta. La cadena no es ni una ruta ni una URL")
        label2.config(text="cadena incorrecta. La cadena no es ni una ruta ni una URL")
        return

def U (cadena):
    print("--> entro al metodo U")
    
    aux = cadena.split('//', 1)
    protocolo = aux[0]
    if len(aux) < 2:
        label2.config(text="URL incorrecto")
        return

    if Protocolo(protocolo):
        print("todo bien con el protocolo")
    else: 
        print("un error con el protocolo")
        return
    
    aux = aux[1].split('/', 1)
    separacion = aux[0].split(':', 1)
    dominio = separacion[0]
    puerto = ""
    
    if len(separacion) > 1:
        puerto = "".join(separacion[1])
        puerto = ":" + str(puerto)

    if Dominio(dominio):
        print("todo bien con el Dominio")
    else: 
        print("un error con el Dominio")
        return
    #Dominio(dominio)

    if Puerto(puerto):
        print("todo bien con el puerto")
    else: 
        print("un error con el puerto")
        label2.config(text="ERROR \n puerto incorrecto")
        return

    print(aux)

    Ruta(aux)
    
    Parametros(aux)

    Etiquetas(aux)

    label2.config(text="URL CORRECTO :)")
    return

def Protocolo(protocolo):
    valor = True
    print("--> Entro a Protocolo")
    if protocolo == "http:":
        print("procolo --> http:")

    elif protocolo == "https:":
        print("procolo --> https:")

    elif protocolo == "ftp:":
        print("procolo --> ftp:")

    elif protocolo == "mailto:":
        print("procolo --> mailto:")

    else:
        #print("Protocolo incorrecto")
        label2.config(text="ERROR: \n protocolo incorrecto")
        valor = False
    return valor
        
def Dominio(dominio):
    valor = True
    print(dominio)
    print("--> entro al Dominio")
    
    aux = dominio.split('.', 2)
    #print(aux)
    if aux[1] in gramatica['X']:
        #N . X E
        
        if N(aux[0]):
            aux.pop(0)
            #print(aux)
            if X(aux[0]):
                aux.pop(0)
                #print("nuevo aux: ", aux)
                E(aux)
            else:
                valor = False
        else:
            valor = False
    else: 
        #Palabra . N . X E
        #print(aux[1], "no es una extencion")

        if Palabra(aux[0]):
            
            aux.pop(0)
            if N(aux[0]):
                aux.pop(0)
                extensiones = "".join(aux)
                extensiones = extensiones.split('.', 1)
                #print(extensiones)
                if X(extensiones[0]):
                    extensiones.pop(0)
                    E(extensiones)
                else: 
                    valor = False
            else: 
                valor = False
        else:
            valor = False
    return valor

def N(nombre):
    valor = True
    print("--> entro a N")
    lista = []
    listaLetras = []
    listaNumeros = []

    nombre = list(nombre)
    #print(nombre)

    for i in nombre:
        #print("caracter a evaluar:", i)
        if i in A_Z or i in a_z:
            if listaNumeros != []:
                lista.append(listaNumeros)
                listaNumeros = []
            #print(i, "es una letra")
            listaLetras.append(i)
        else:
            if listaLetras != []:
                lista.append(listaLetras)
                listaLetras = []

            if i in O_9:
                #print(i, "es un numero")
                listaNumeros.append(i)
            else:
                print(i, "NO ES NI LETRA NI NUMEROOOO")
                texto = "ERROR: \n " + i + "No es una letra o número"
                label2.config(text=texto)
                valor = False
                
                
    if listaNumeros != []:
        lista.append(listaNumeros)
    if listaLetras != []:
        lista.append(listaLetras)
    print(lista)

    for i in lista:
        if i[0] in A_Z or i[0] in a_z:
            nombre =  "".join(i)
            Palabra(str(nombre))
        elif i[0] in O_9:
            nombre =  "".join(i)
            Numero(str(nombre))
        else:
            print(i[0], " NO ES NI NUMERO NI LETRAAAAA")
            texto = "ERROR: \n " + i[0] + "No es una letra o número"
            label2.config(text=texto)
            valor = False
    return valor

def E(extensiones):
    valor = True
    print("--> entro a la extensiones")
    extensiones = "".join(extensiones)
    #print(extensiones)

    if extensiones != "":
        extensiones = extensiones.split('.')
        for i in extensiones:
            if X(i):
                valor = True
            
    return valor        

def X(extension):
    valor = True
    print("--> entro a X")
    if extension in tokens['Extension']:
        print(extension, "es una extension")
    else: 
        texto = "ERROR: \n " + extension + "No es una extensión"
        label2.config(text=texto)
        valor = False
    return valor

def Puerto(puerto):
    valor = True
    print("--> entro al metodo Puerto")
    print(puerto)
    if puerto != '':
        if puerto[0] == ':' : 
            puerto = puerto.split(":")
            puerto.pop(0)
            #print(puerto)
            puerto = "".join(puerto)
            if Numero(str(puerto)):
                valor = True
            else:
                valor = False 
    return valor
        
            
def Ruta(cadena):
    #recibe una lista ['www.github.com.mx', 'danielTeniente/ia-projects/blob/main/Algoritmos_geneticos/Maximizar_funcion.ipynb']
    print("--> Entro a Ruta")
    if len(cadena) > 1 :
        ruta = cadena[1].split("#",1)
        ruta = ruta [0].split("?",1)
        ruta = "".join(ruta[0])
        print("ruta -->", ruta)
        if ruta != '':
            print("existe la ruta")
            for i in ruta:
                if i == '_' or i == '-' or i == '.' or i == '/' or i in a_z or i in A_Z or i in O_9:
                    i = i
                else:
                    print(i," NO ES NI LETRA, NI NUMERO, NI _, -, ., /")
                    exit(0)      

        else: 
            print("no exite ruta en la cadena")

def Parametros(cadena):
    print("--> entro a Parametros")
    parametros = cadena[1].split("#",1)
    parametros = parametros[0].split("?",1)
    if len(parametros) > 1 :
        parametros = "".join(parametros[1])
        print(parametros)

    else:
        print("No se encontraron parametros")

def P(parametros):
    for i in parametros:
        if i == '=' or i == '+' or i == '&' or i == '%' or Let(i) or Dig(i):
            i = i
        else: 
            print("no exiten parametros en la cadena")
 
def Etiquetas(cadena):
    print("--> entro a etiquetas")
    print(cadena[1])
    etiquetas = cadena[1].split('#')
    print(etiquetas)

    if len(etiquetas) > 1 :
        etiquetas = "".join(etiquetas)
        Et(etiquetas)
    else: 
        print("no exiten etiquetas en la cadena")

def Et(etiquetas):
    for i in etiquetas:
        if i == '=' or i == '-' or i == '_' or i == '.' or i == '/' or Let(i) or Dig(i):
            i = i


def R(cadena):
    texto = cadena
    print("--> Entro a R")
    cadena = cadena.split('\\', 1)
    unidad = cadena[0]
    texto = "".join(cadena[1])
    #print(cadena)

    if Lunidad(unidad):
        print("todo bien con la unidad")
    else: 
        return

    ruta = cadena[1]
    ruta = ruta.split('\\')
    num = len(ruta) - 1
    archivo = ruta.pop(num)
    
    ruta = texto.replace(str(archivo), "")
    #print( " Nueva ruta ", ruta)

    if Carpeta(ruta):
        print("todo bien con la carpeta")
    else: 
        return

    if '.' in archivo:
        print(archivo, "si es archivo")
        if Archivo(archivo):
            print("todo bien con el archivo")
        else: 
            return
        label2.config(text="RUTA A ARCHIVO CORRECTO :)")   
    else:
        texto = "ERROR: \n " + archivo + " no es un archivo"
        label2.config(text=texto)
    
    return

def Lunidad(unidad):
    valor = True
    print(unidad)
    if len(unidad) == 2:
        if unidad[0] in A_Z:
            print(unidad[0], "si es una letra")
            if unidad[1] == ':':
                print("se encontro :")
                
            else: 
                #print("no se encontro el :")
                label2.config(text="ERROR: \n no se encontro el :")
                valor = False
        else: 
            #print(unidad[0], "NO ES UNA LETRA MAYUSCULAAAA")
            texto = "ERROR: \n" + unidad[0] + "no se encontro el :"
            label2.config(text=texto)
            valor = False
    else: 
        #print("Unidad no encontrada")
        label2.config(text="ERROR: \n Unidad no encontrada")
        valor = False
    return valor

def Carpeta (carpetas):
    valor = True
    print("--> entro a Carpeta")

    for i in carpetas: 
        if Let(i) or Dig(i) or i == '\\' or i == '_':
            print(i, end="")
        else: 
            print()
            texto = "ERROR: \n " + i + "No es un caracter aceptado para la ruta de carpetas."
            label2.config(text=texto)
            valor = False
    print()
    return valor

def Archivo(archivo):
    valor = True
    print("--> entro a Archivo")
    for i in archivo: 
        if Let(i) or Dig(i) or i == '_':
            print(i, end="")
        elif i == '.':
            ext = archivo.split('.')
            if len(ext) > 2:
                
                label2.config(text="ERROR: \n Se detectó más de una extención")
                valor = False
            else:
                ext = "".join(ext[1])
                if Palabra(ext[1]):
                    valor = True
                else:
                    label2.config(text="ERROR: \n Extencion de archivo incorrecto")
                    valor = False
        else: 
            print()
            texto = "ERROR: \n " + i + "no es un caracter aceptado para la ruta de carpetas."
            label2.config(text=texto)
            valor = False
    print()
    return valor

def Palabra(palabra):
    valor = True
    print("--> entro a Palabra")

    palabra = list(palabra)
    #www --> [w, w, w]
    if len(palabra) > 0:
        if Let(palabra[0]):
            palabra.pop(0)
            Rlet(palabra)
        else: 
            valor = False
    else: 
        valor = False
    return valor

def Rlet(letras):
    print("--> entro a Rlet")

    contador = 0
    if len(letras) > 0:
        for i in letras:
            #print("se manda la posicion", contador, "de la lista ", letras)
            Let(i)
            
def Let(letra):
    valor = True
    print("--> entro a Let")

    if letra in A_Z:
        print(letra, "si se encuetra dentro de letras de la A-Z")

    elif letra in a_z:
        print(letra, "si se encuetra dentro de letras de la a-z")

    else:
        print(letra, "NO ES LETRAAAA")
        valor = False
    return valor
        
def Numero(numeros):
    valor = True
    print("--> entro a Numero")

    digitos = list(numeros)
    #345 --> [3, 4, 5]
    if len(digitos) > 0:
        if Dig(digitos[0]):
            digitos.pop(0)
            Rdig(digitos)
        else:
            valor = False
    else:
        valor = False
    return valor

def Rdig(digitos):
    print("--> entro a Rdig")

    if len(digitos) > 0:
        for i in digitos:
            Dig(i)

def Dig(digito):
    valor = True
    print("--> entro a Dig")

    if digito in O_9:
        print(digito, "es un numero")
    else: 
        print(digito, "NO ES UN NUMEROOOO")
        texto = digito, "No es un número"
        label2.config(text=texto)
        valor = False

    return valor

        #exit(0)


    

    



ventana = tk.Tk()
ventana.geometry("1300x700")
ventana.resizable(0, 0)
ventana.title("Analizador lexico")
label = tk.Label(ventana, text="Ingrese URL/Ruta: ", font="Helvetica 20")
label.pack()
label.place(relx=0.01, rely=0.01)
input = tk.Entry(ventana, font="Helvetica 16")
input.pack()
input.place(relx=0.1, rely=0.09, relheight=0.07, relwidth=0.77)


#input.insert(0, "C:\carpeta1\carpeta2\\archivo1.doc")
input.insert(0, "https://www.github.com.mx:80/danielTeniente/ia-projects/blob/main/Algoritmos_geneticos/Maximizar_funcion.ipynb?v=PP20rtarbuc#slide=id.g1114567e7cc")


boton1 = tk.Button(ventana, text="Analizador Léxico", command=lambda: AnalisisLexico(input.get()))
#boton1 = tk.Button(ventana, text="Analizador Léxico", command=lambda: AnalisisLexico('C:\carpeta1\carpeta2\archivo1.doc'))
boton1.pack()
boton1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.15)


boton2 = tk.Button(ventana, text="Analizador Sintáctico", command=lambda: AnalisisSintactico(input.get()))
boton2.pack()
boton2.place(relx=0.3, rely=0.2, relheight=0.1, relwidth=0.15)
#boton2["state"] = "disabled"

boton3 = tk.Button(ventana, text="Abrir", command=lambda: AnalisisLexico(input.get()))
boton3.pack()
boton3.place(relx=0.5, rely=0.2, relheight=0.1, relwidth=0.15)
boton3["state"] = "disabled"

label2 = tk.Label(ventana, text="", font="Helvetica 15")
label2.pack()
label2.place(relx=0.4, rely=0.45)

label3 = tk.Label(ventana, text="Resultados del analizador sintáctico:", font="Helvetica 15")
label3.pack()
label3.place(relx=0.4, rely=0.4)

frame1 = tk.LabelFrame(ventana, text="Análisis Léxico")
frame1.place(height=350, width=400, rely=0.4, relx=0.05)

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)


ventana.mainloop()



