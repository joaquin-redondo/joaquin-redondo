# Un instituto de inglés necesita un programa que le permita, cada día, procesar
# observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
# distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se
# dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los
# jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
# Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
# DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
# número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
# día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
# que se produjo un error. Debe permitirse que ingrese el día de la semana en
# minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
# ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
# Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
# exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
# que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
# exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
# programa le mostrará el porcentaje de aprobados.
# Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
# porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
# que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.
# Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
# mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
# la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
# imprimir el ingreso total en $.
def arreglo(): 
    try:
        fecha_ingresada = input("Ingrese la fecha respetando este formato: día, DD/MM: ").strip()
        dia, fecha = fecha_ingresada.split(", ")
        dia = dia.lower()
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
        if dia not in dias_semana:
            raise ValueError("Día de la semana inválido.")
        
        numero_dia, numero_mes = map(int, fecha.split("/"))
        if numero_dia > 31 or numero_mes > 12:
            raise ValueError("Fecha inválida.")
        
        if dia == "lunes":
            procesar_nivel("inicial")
        elif dia == "martes":
            procesar_nivel("intermedio")
        elif dia == "miércoles":
            procesar_nivel("avanzado")
        elif dia == "jueves":
            porcentaje_asistencia = float(input("Ingrese el porcentaje de asistencia %"))
            if porcentaje_asistencia > 50:
                print("Asistió la mayoría.")
            else:
                print("No asistió la mayoría.")
        elif dia == "viernes":
            if (numero_dia == 1 and numero_mes == 1) or (numero_dia == 1 and numero_mes == 7):
                print("Comienzo de nuevo ciclo")
                alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                cuota_por_alumno = float(input("Ingrese la cuota en $ por cada alumno: "))
                ingreso_total = alumnos_nuevo_ciclo * cuota_por_alumno
                print(f"Ingreso total en $: {ingreso_total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    
def procesar_nivel(nivel):
    rinde_prueba = nivel in ["inicial", "intermedio", "avanzado"]
    if rinde_prueba:
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados= int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = aprobados + desaprobados
        porcentaje_aprobados = (aprobados / total_alumnos) * 100
        print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")

if __name__ == "__main__":
    arreglo()
