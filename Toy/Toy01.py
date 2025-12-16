
import random

archivos = ["adjetivos.txt","comidas.txt","lugares.txt","nombres.txt","oficios.txt","puestos.txt","sentimientos.txt"]
lista_adjetivos = []
lista_comidas = []
lista_lugares = []
lista_nombres = []
lista_oficios = []
lista_puestos = []
lista_sentimientos = []
listas = [lista_adjetivos, lista_comidas, lista_lugares, lista_nombres, lista_oficios, lista_puestos, lista_sentimientos]
palabras_historia = []

# Leer archivo y convertir a lista
for i in range(len(listas)):
    with open(archivos[i], "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()
        # Crear lista (evita elementos vacíos si el archivo está vacío)
        listas[i] = [p.strip() for p in contenido.split(",") if p.strip()]

while(True):
    palabras_historia = []
    print("¿Deseas personalizar la historia o generarla aleatoriamente?\n1.Personalizar\n2.Sorpréndeme!\n\n0.Salir")
    opcion = int(input())
    if opcion == 1:
        #Se recorren todas las categorias de palabras
        for i in range(len(listas)):
            lista_minus = []
            string = archivos[i][slice(0,len(archivos[i])-5)]
            if i == 0 or i == 1 or i == 2:
                #Se piden 2 veces alguna comida, adjetivo y lugar
                for j in range(2):
                    print(f"Ingrese un / una {string} por favor")
                    nuevo = input("")
                    lista_minus = [p.lower() for p in listas[i]] 
                    #Se añaden nuevas palabras a un txt evitando repetición y sin importar mayusculas
                    if nuevo.lower() not in lista_minus:
                        listas[i].append(nuevo)
                        with open(archivos[i], "w", encoding="utf-8") as archivo:
                            archivo.write(",".join(listas[i]))
                        palabras_historia.append(nuevo)

                    else:
                        palabras_historia.append(nuevo)
            else:
                print(f"Ingrese un {string} por favor")
                nuevo = input("")
                lista_minus = [p.lower() for p in listas[i]] 
                #Se añaden nuevas palabras a un txt evitando repetición y sin importar mayusculas
                if nuevo.lower() not in lista_minus:
                    listas[i].append(nuevo)
                    with open(archivos[i], "w", encoding="utf-8") as archivo:
                        archivo.write(",".join(listas[i]))
                    palabras_historia.append(nuevo)
                else:
                    palabras_historia.append(nuevo)
        #Imprime la historia con las palabras dadas
        historia = print(f"\n{palabras_historia[6].capitalize()} visitó el {palabras_historia[4]} para buscar a un {palabras_historia[7]} {palabras_historia[0]} que conoció en su niñez.\nÉl la invitó a caminar hacia el {palabras_historia[5]}, donde compartieron {palabras_historia[2]} y {palabras_historia[3]} mientras recordaban historias.\nEn medio del silencio {palabras_historia[1]}, {palabras_historia[6].capitalize()} sintió {palabras_historia[9]}.\n")
    if opcion == 2:
        for i in range(len(listas)):
            if i == 0 or i == 1 or i == 2:
                #Se elige aleatoriamente 2 veces alguna comida, adjetivo y lugar
                for j in range(2): 
                    with open(archivos[i], "r", encoding="utf-8") as archivo:
                        contenido = archivo.read()
                    lista_palabras = [p.strip() for p in contenido.split(",") if p.strip()]
                    palabra_aleatoria = random.choice(lista_palabras)
                    palabras_historia.append(palabra_aleatoria)
            else:
                with open(archivos[i], "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                lista_palabras = [p.strip() for p in contenido.split(",") if p.strip()]
                palabra_aleatoria = random.choice(lista_palabras)
                palabras_historia.append(palabra_aleatoria)
        #Imprime la historia con las palabras seleccionadas aleatoriamente
        historia = print(f"\n{palabras_historia[6].capitalize()} visitó el {palabras_historia[4]} para buscar a un {palabras_historia[7]} {palabras_historia[0]} que conoció en su niñez.\nÉl la invitó a caminar hacia el {palabras_historia[5]}, donde compartieron {palabras_historia[2]} y {palabras_historia[3]} mientras recordaban historias.\nEn medio del silencio {palabras_historia[1]}, {palabras_historia[6].capitalize()} sintió {palabras_historia[9]}.\n")
    if opcion == 0:
        print("Hasta pronto!\n")
        break
