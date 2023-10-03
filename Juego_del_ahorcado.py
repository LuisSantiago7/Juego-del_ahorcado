from random import choice
from time import sleep

intentos = 0 
max_intentos = 6
vidas = ['❤️  ❤️  ❤️  ❤️  ❤️  ❤️', '❤️  ❤️  ❤️  ❤️  ❤️  🖤', '❤️  ❤️  ❤️  ❤️  🖤  🖤', '❤️  ❤️  ❤️  🖤  🖤  🖤', '❤️  ❤️  🖤  🖤  🖤  🖤', '❤️  🖤  🖤  🖤  🖤  🖤', '🖤  🖤  🖤  🖤  🖤  🖤']

#Funcion para que el programa elija la palabra secreta
def choice_words():
     words = ["guitarra", "montaña", "computadora", "bicicleta", "pastel", "playa", "libro", "perro", "paracaídas", "espejo", "carpeta", "sombrero", "teléfono", "silla", "pintura", "árbol", "muñeca", "cuchillo", "vaso", "diamante", "café", "abrazo", "papaya", "cama", "televisor", "lámpara", "globo", "dinero", "manzana", "avión", "barco", "piano", "medicina", "jardín", "tienda", "martillo", "fuego", "coche", "piscina", "clima", "maní", "lentes", "pelota", "teatro", "chocolate", "zapatos", "botella", "desierto"]
     random_word = choice(words)
     lista_palitos = ['-' for i in random_word]
     return lista_palitos, random_word
 


#Funcion de animacion de carga xd
def animacion_carga():
                    cargando = True
                    while cargando:
                        for i in range(4):
                            print("Cargando" + "." * i, end="\r")
                            sleep(0.3)
                        cargando = False
                    print(end="") 
#Funcion que pregunta al usuario si esta listo para poder ejecutar el juego
def pregunta_usuario():
        while True:
                listo = input('¿Estás listo? (y/n)\n').lower()
                if listo == 'y':
                        animacion_carga()
                        print('Ya pensé en una palabra secreta, adivinala letra por letra.\nRecuerda, solo tienes 6 vidas')  
                        return True  
                elif listo == 'n':
                        animacion_carga()
                        print('¿Como que no estas listo?, empecemos de nuevo')
#Funcion que Presenta la palabra oculta, junto con las vidas iniciales
def presentacion(word_fade, word_secret):
    print('-'*80)
    print(f'Vidas: {vidas[0]}')
    print(word_fade)
    
    
#Funcion de rondas
def rondas(word_fade, word_secret):
    global intentos
    
    word_secret = list(word_secret)
    
    letra_1 = input('Primer intento\n').lower()
    
    if letra_1 in word_secret:
        for i in range(len(word_secret)):
            if letra_1 == word_secret[i]:
                word_fade[i] = letra_1
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_1} sí estáen la palabra secreta!')
                print(word_fade)
    else:
        print(f'UPS, la letar {letra_1} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
        
    letra_2 = input('Segundo intento\n').lower()
    
    if letra_2 in word_secret:
        for i in range(len(word_secret)):
            if letra_2 == word_secret[i]:
                word_fade[i] = letra_2
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_2} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
                
    else:
        print(f'UPS, la letar {letra_2} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')      


    letra_3 = input('Tercer intento\n').lower()
    
    if letra_3 in word_secret:
        for i in range(len(word_secret)):
            if letra_3 == word_secret[i]:
                word_fade[i] = letra_3
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_3} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_3} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
        
    letra_4 = input('Cuarto intento\n').lower()
    
    if letra_4 in word_secret:
        for i in range(len(word_secret)):
            if letra_4 == word_secret[i]:
                word_fade[i] = letra_4
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_4} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_4} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
    letra_5 = input('Quinto intento\n').lower()
    
    if letra_5 in word_secret:
        for i in range(len(word_secret)):
            if letra_5 == word_secret[i]:
                word_fade[i] = letra_5
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_5} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_5} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
    letra_6 = input('Sexto intento\n').lower()
    
    if letra_6 in word_secret:
        for i in range(len(word_secret)):
            if letra_6 == word_secret[i]:
                word_fade[i] = letra_6
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_6} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_6} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
           
    letra_7 = input('Septimo intento\n').lower()
    
    if letra_7 in word_secret:
        for i in range(len(word_secret)):
            if letra_7 == word_secret[i]:
                word_fade[i] = letra_7
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_7} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_7} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
    letra_8 = input('Octavo intento\n').lower()
    
    if letra_1 in word_secret:
        for i in range(len(word_secret)):
            if letra_8 == word_secret[i]:
                word_fade[i] = letra_8
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_8} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_8} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
    letra_9 = input('Noveno intento\n').lower()
    
    if letra_9 in word_secret:
        for i in range(len(word_secret)):
            if letra_9 == word_secret[i]:
                word_fade[i] = letra_9
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_9} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
    else:
        print(f'UPS, la letar {letra_9} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
        
    letra_10 = input('Décimo intento\n').lower()
    
    if letra_10 in word_secret:
        for i in range(len(word_secret)):
            if letra_10 == word_secret[i]:
                word_fade[i] = letra_10
                print(f'Vidas: {vidas[intentos]}')
                print(f'Correcto, la letra {letra_10} sí estáen la palabra secreta!')
                print(word_fade)
            if word_fade == word_secret:
                print(f'Felicidades! descubriste la palabra secreta\n {word_secret}')
                break
            
    else:
        print(f'UPS, la letar {letra_10} no está en la palabra secreta')
        intentos += 1
        print(f'Vidas: {vidas[intentos]}')
                
                
    
    
     

#LOOP juego
while intentos < max_intentos:
    word_fade, word_secret = choice_words()
    animacion_carga()
    pregunta_usuario()
    presentacion(word_fade, word_secret )
    rondas(word_fade, word_secret)


    
    
            

'''def rondas(word_fade, word_secret):
    global intentos

    word_secret = list(word_secret)

    for i in range(max_intentos):
        letra = input(f'Intento {i + 1}\n').lower()

        if letra in word_secret:
            for j in range(len(word_secret)):
                if letra == word_secret[j]:
                    word_fade[j] = letra
            print(f'Correcto, la letra {letra} sí está en la palabra secreta!')
            print(word_fade)

            if word_fade == word_secret:
                print(f'¡Felicidades! Descubriste la palabra secreta: {"".join(word_secret)}')
                return

        else:
            print(f'UPS, la letra {letra} no está en la palabra secreta')
            intentos += 1
            print(f'Vidas: {vidas[intentos]}')

    print('Se agotaron los intentos. ¡Perdiste!')
    print(f'La palabra secreta era: {"".join(word_secret)}')
'''
