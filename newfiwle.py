import matplotlib.pyplot as plt
import numpy as np
import time
import os

def grafico(vi,ac,tm):
    fig, (gf1, gf2) = plt.subplots(2, 1)
    X = np.linspace(0, tm)
    fig.suptitle(None)

    Y1 = vi * X + 0.5 * ac * (X ** 2)  # Formula distancia
    gf1.plot(X, Y1, marker=".", color="red")
    gf1.grid()
    gf1.set_title("Distancia")
    gf1.set_ylabel("Metros")
    gf1.set_xlabel("Segundos")

    Y2 = (ac * X) + vi  # Formula velocidad
    gf2.plot(X, Y2, marker=".")
    gf2.grid()
    gf2.set_title("Velocidad")
    gf2.set_ylabel("Metros/segundo")
    gf2.set_xlabel("Segundos")

    plt.subplots_adjust(hspace=0.6)
    plt.show()

dis_total=0
while True:
    num_etapas = int(input("Ingrese el numero de etapas: "))
    if num_etapas >= 3: break #condición
    print("Tiene que ser mayor a 3 jaja")
for i in range(num_etapas):

    print(f"Inicio de la etapa n°{i+1}")

    n_no = 0 #Solo puede decir que no sabe una variable una vez

    #aceleracion
    acel_ver=input("Sabe la aceleracion?(Si/No): ")
    if acel_ver.lower()=="si":
        tf_acel = True
        acel = float(input("Introduzca la aceleracion: "))
    else:
        tf_acel = False
        n_no+=1

    #tiempo
    if n_no == 0:
        tiempo_ver=input("Sabe el tiempo?(Si/No): ")
        if tiempo_ver.lower()=="si":
            tf_tiempo = True
            tiempo = float(input("Introduzca el tiempo: "))
        else:
            tf_tiempo = False
            n_no+=1
    else:
        tf_tiempo = True
        tiempo = float(input("Introduzca el tiempo: "))

    # Velocidad inicial
    if i == 0: #La velocidad inicial se pregunta solo la primera vez*
        if n_no == 0:
            vel_ini_ver=input("Sabe la Velocidad Inicial?(Si/No): ")
            if vel_ini_ver.lower()=="si":
                vel_ini = float(input("Introduzca la velocidad inicial: "))
                tf_vel_ini = True
            else:
                tf_vel_ini = False
                n_no+=1
        else:
            vel_ini = float(input("Introduzca la velocidad inicial: "))
            tf_vel_ini = True
    else: #si no es la primera vez, se "saca" de la velocidad final de la etapa anterior
        if tf_vel_fin==True: vel_ini = vel_fin
        elif tf_vel_fin==False: vel_ini = vel_fin

    #Velocidad final
    if tf_acel==True and tf_tiempo==True and tf_vel_ini==True:
            tf_vel_fin = False
    else:
        if acel==0 and tf_tiempo==False:
            print("Tiempo indeterminable porque la velocidad final no cambia, se pasa a la sig. etapa")
            tf_vel_fin = True
            vel_fin = vel_ini
            continue
        if n_no==0:
            vel_fin_ver=input("Sabe la Velocidad Final?(Si/No): ")
            if vel_fin_ver.lower()=="si":
                vel_fin = float(input("Introduzca la velocidad final: "))
                tf_vel_fin = True
        else:
            tf_vel_fin = True
            vel_fin = float(input("Introduzca la velocidad final: "))
            tf_vel_fin = True

    ###CALCULOS###

    # calculo velocidad final
    if tf_vel_fin==False:
        vel_fin = (acel*tiempo)+vel_ini
        if acel<0: vel_fin=0
        print("La velocidad final es de:",vel_fin)

    # calculo velocidad inicial
    if tf_vel_ini==False:
        vel_ini = vel_fin-acel*tiempo
        print("La velocidad inicial es de:",vel_ini)

    # calculo tiempo
    if tf_tiempo==False:
        tiempo = (vel_fin-vel_ini)/acel
        print("El tiempo es de:",tiempo)

    # calculo aceleracion
    if tf_acel==False:
        acel = (vel_fin-vel_ini)/tiempo
        print("La aceleracion es de:",acel)


    dis_etapa = vel_ini*tiempo+0.5*acel*(tiempo**2)
    print(f"La distancia recorrida es de: {dis_etapa}\n")
    dis_total += dis_etapa
    time.sleep(1)

    grafico(vel_ini,acel,tiempo)

    input("Enter para continuar")
    os.system('cls')
