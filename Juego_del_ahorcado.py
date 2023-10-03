from random import randint 
import time
print('\n                             BUSCA EL NUMERO SECRETO.                    ')
name = input('Ingresa tu nombre\n')
print(f'''Hola, {name.capitalize()} las reglas del juego son muy simples.
Yo como computadora, pensaré en un número aleatorio entre el 1 al 100 y tu tendrás que adivinarlo, tendrás solo 8 intentos''')
while True:
    conf_user = input('¿Estás listo? (yes/no) \n').capitalize()
    if conf_user == 'Yes':
        def animacion_carga():
            cargando = True
            while cargando:
                for i in range(4):
                    print("Cargando" + "." * i, end="\r")
                    time.sleep(0.5)
                cargando = False
            print(end="")   
        animacion_carga()      
        num_random = randint(1,100)
        print('Ya pensé en un número')
        intentos_inicial = 8
        intentos_final = 0
        if intentos_inicial <= 8 and intentos_inicial > 0:
            while intentos_inicial > 0 and intentos_inicial <=8:
                num_user = int(input('¿Adivina cúal es entre el 1 y el 100?\n'))
                if num_user < 1 or num_user > 100:
                    print('Ese número está fuera del rango, no es valido')
                    intentos_inicial -= 1
                    intentos_final += 1
                    print(f'Te quedan {intentos_inicial} intentos')
                elif num_user < num_random:
                    print('Ese número es menor al número que elegí ⬇️  🤭')
                    intentos_inicial -= 1
                    intentos_final += 1
                    print(f'Te quedan {intentos_inicial} intentos')
                elif num_user > num_random: 
                    print('Ese número es mayor al número que elegí ⬆️  🤭')
                    intentos_inicial -= 1
                    intentos_final += 1
                    print(f'Te quedan {intentos_inicial} intentos')
                elif num_user == num_random:
                    print('Felicidades, adivinaste el número secreto 🥳')
                    if intentos_final == 1:
                        print(f'Solo hiciste {intentos_final} intento')
                    elif intentos_final > 1 and intentos_final < 8:
                        print(f'Solo hiciste {intentos_final} intentos')     
                        break       
        break            
    elif conf_user == 'No': 
        print('Como no vas a estarlito... va de nuevo xd')
    else:
        print('Por favor confirma si estas listo o no xd')  
          

