def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    
    horas_en_segundos = 3600

    horas = total_segundos//(horas_en_segundos)
    minutos = total_segundos%(horas_en_segundos)//60
    segundos = total_segundos%(horas_en_segundos)%60

    print(horas)
    print(minutos)
    print(segundos)

