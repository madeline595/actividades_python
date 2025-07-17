
import random
import string
"""Importación del archivo de palabras"""
from palabras import palabras
from muñeco import vidas




def obtener_palabra_valida(palabras):    
  


  palabra = random.choice (palabras)
  
  
  while '-' in palabra or ' ' in palabra:
   palabra = random.choice(palabras)
  return palabra.upper()






def muñeco():
  print("==============================")
  print("¡Bienvenido(a) al juego deel ahorcado!")
  print("==============================")

  palabra = obtener_palabra_valida(palabras)
  letras_por_adivinar = set(palabra)
  abecedario = set(string.ascii_uppercase)
  letras_adivinadas = set()

  vidas = 7

  while len(letras_por_adivinar) >0 and vidas > 0:
    print(f"Te quedan {vidas} vidas y has usado esras letras:{' '.join(letras_adivinadas)}")

    palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
    print(vidas_diccionario_visual[vidas])
    print(f"palabra:{' '.jpin(palabra_lista)}")

    letra_usuario = input('Escoge una letra:').upper()


    if letra_usuario in abecedario - letras_adivinadas:
      letras_adivinadas.add(letra_usuario)

      if letra_usuario in letras_por_adivinar:
        letras_por_adivinar.remove(letra_usuario)
        print('')

      else:
        vidas = vidas - 1
        print('')

    elif letra_usuario in letras_adivinadas:
      print("\nYa escogiste esa letra . Por favor escoge una letra nueva .")

  












