def cal_dist(v,t,a):
    val= v*t+0.5*a*(t**2)
    return val

dis_total=0
while True:
    num_etapas = int(input("Ingrese el numero de etapas: "))
    if num_etapas >= 3: break
    print("NOO")
for i in range(num_etapas):

    print(f"Inicio de la etapa n°{i+1}")
    
    n_no = 0

    #aceleracion
 
    acel_ver=input("Sabe la aceleracion?(Si/No):\n ")
    if acel_ver.lower()=="si":
        tf_acel = True
        acel = float(input("Introduzca la aceleracion: "))
    else:
        tf_acel = False
        n_no+=1
        print("")

    #tiempo
    if n_no == 0:
        tiempo_ver=input("Sabe el tiempo?(Si/No):\n ")
        if tiempo_ver.lower()=="si":
            tf_tiempo = True
            tiempo = float(input("Introduzca el tiempo: "))
        else:
            tf_tiempo = False
            print("")
            n_no+=1
    else: 
        tf_tiempo = True
        tiempo = float(input("Introduzca el tiempo: "))
    
    ## ESTO ES UN COMETARIO
   
    if i == 0: 
        #Velocidad inicial
        if n_no == 0:
            vel_ini_ver=input("Sabe la Velocidad Inicial?(Si/No):\n ")
            if vel_ini_ver.lower()=="si":
                vel_ini = float(input("Introduzca la velocidad inicial: "))
                tf_vel_in = True
            else:
                tf_vel_in = False
                n_no+=1
                print("")
        else: 
            vel_ini = float(input("Introduzca la velocidad inicial: "))
            tf_vel_in = True
    else: 
        if tf_vel_fin==True: vel_ini = vel_fin 
        elif tf_vel_fin==False: vel_ini = vel_fin
    
    #Velocidad final
    if tf_acel==True and tf_tiempo==True and tf_vel_in==True:
            tf_vel_fin = False
    else:
        if n_no==0:
            vel_fin_ver=input("Sabe la Velocidad Final?(Si/No):\n ")
            if vel_fin_ver.lower()=="si":
                vel_fin = float(input("Introduzca la velocidad final: "))
                tf_vel_fin = True
        else:
            tf_vel_fin = True 
            vel_fin = float(input("Introduzca la velocidad final: "))
            tf_vel_fin = True

    if tf_vel_fin==False:
        #calculo velocidad final
        vel_fin = (acel*tiempo)+vel_ini
        if acel<0: vel_fin=0
        print("La velocidad final es de:",vel_fin)
        
    if tf_vel_in==False:
        #calculo velocidad inicial
        cal_vi = vel_fin-acel*tiempo 
        print("La velocidad inicial es de:",cal_vi)

    if tf_tiempo==False:
        #calculo tiempo
        tiempo = (vel_fin-vel_ini)/acel
        print("El tiempo es de:",tiempo)

    if tf_acel==False:
        #calculo aceleracion
        acel = (vel_fin-vel_ini)/tiempo
        print("La aceleracion es de:",acel)

    print(f"La distancia recorrida es de: {cal_dist(vel_ini, tiempo, acel)}")
    dis_total += cal_dist(vel_ini, tiempo, acel)