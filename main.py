from datetime import datetime

actual = datetime.now()


# desde la rama main
# ----------------> main
def main():

    print(f'Hora actual: {actual.hour}.{actual.minute}\n')

    hora = int(input("Ingresar la hora: "))
    min = int(input("Ingresar los minutos: "))

    print(calculo(hora, min))


def calculo(hora, minuto): 
    min_sobrante = 0


    # los minutos sobrantes no los devuelve bien
    # resolverlo usando % guardandolo y usando el resto
    # como una suma del minuto actual
    
    if actual.minute + minuto >= 60:
        hora +=((actual.minute + minuto) // 60)
        min_sobrante = (actual.minute + minuto) % 60
        if min_sobrante // 10 == 0:
            return f'Hora: {hora + actual.hour}:0{min_sobrante}'    
        return f'Hora: {hora + actual.hour}:{min_sobrante}'
    else:
        if min_sobrante + minuto // 10 == 0:
            return f'Hora: {actual.hour + hora}:{minuto + min_sobrante}'    
        return f'Hora: {actual.hour + hora}:{minuto + actual.minute}'

if __name__ == "__main__":
    main()


'''
1. Arreglar el problema de los minutos.
2. cada multiplo de 60 en minuto es un +1 en hora. ej hora: 3 min: 128 resultado 5.8
3. cada multiplo de 24 en hora es un +1 en dia.
4(final). Adaptarlo a Tkinter
'''

# rama python a ver que ondis

