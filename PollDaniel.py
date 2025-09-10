print("====================================================================================")
print(r"""
  ______                            _                                        
 |  ____|                          | |                                       
 | |__   _ __   ___ _   _  ___  ___| |_ __ _                                 
 |  __| | '_ \ / __| | | |/ _ \/ __| __/ _` |                                
 | |____| | | | (__| |_| |  __/\__ \ || (_| |                                
 |______|_| |_|\___|\__,_|\___||___/\__\__,_|                                
  _____                                 _ _           _                      
 |  __ \                               | | |         | |                     
 | |  | | ___  ___  __ _ _ __ _ __ ___ | | | __ _  __| | ___  _ __ ___  ___  
 | |  | |/ _ \/ __|/ _` | '__| '__/ _ \| | |/ _` |/ _` |/ _ \| '__/ _ \/ __| 
 | |__| |  __/\__ \ (_| | |  | | | (_) | | | (_| | (_| | (_) | | |  __/\__ \ 
 |_____/ \___||___/\__,_|_|  |_|  \___/|_|_|\__,_|\__,_|\___/|_|  \___||___/ 
      | |           (_)                                                      
      | |_   _ _ __  _  ___  _ __                                            
  _   | | | | | '_ \| |/ _ \| '__|                                           
 | |__| | |_| | | | | | (_) | |                                              
  \____/ \__,_|_| |_|_|\___/|_|                                              
                                                                             
                                                                             """)
print("====================================================================================\n")
print('''La siguiente es una encuesta que tiene como objetivo dar consejos a los jovenes entre 18 y 20 años o mayores.''')

#TAREA: Realizar una encuesta a sus compañeros: 
#---->  si la persona es mayor o igual de 18 años proporcione un consejo de economia 
#---->  si la persona es igual o mayor de 20 de un consejo de amor


cont = "si"
while(cont == "si"):
    name = input("¿Como te llamas?\n")
    age = int(input("¿Que edad tienes?\n"))
    if (18 <= age < 20):
            mood = int(input(f"Como te sientes el dia de hoy con respecto a tus finanzas {name}? del 1 al 5, siendo 1 'Terrible' y siendo 5 'Excelente' "))
        
            if (mood == 1 ): 
                print("“No ahorres lo que queda después de gastar, sino gasta lo que queda después de ahorrar.”\n - Adam Smith, La riqueza de las naciones")
            elif(mood == 2):
                print("“No es la falta de riquezas lo que produce la pobreza, sino la multiplicación de deseos.”\n - Séneca, Epistulae Morales ad Lucilium")
            elif(mood == 3):
                print("“Un viaje de mil millas comienza con un solo paso.”\n - Confucio, citado en Analectas")
            elif(mood == 4):
                print("“No ahorres lo que queda después de gastar, sino gasta lo que queda después de ahorrar.”\n - Buffett, W. (2008). Entrevista en Forbes Magazine.")
            elif(mood == 5):
                print("“Cuidado con los pequeños gastos; una pequeña fuga hunde un gran barco.”\n - Benjamin Frankin.")
        
    elif (age >= 20):
        mood = int(input(f"¿Cómo te sientes el día de hoy con respecto al amor {name}? Del 1 al 5, siendo 1 'terrible' y 5 'excelente': "))

        if mood == 1:
            print("“Estas penas de amor que parecen dulces, en realidad se vuelven más crueles con el tiempo.”\n - William Shakespeare, Romeo y Julieta.")
        elif mood == 2:
            print("“No ser amado es una simple desventura. La verdadera desgracia es no saber amar.”\n - Albert Camus, El mito de Sísifo.")
        elif mood == 3:
            print("“Ama, no como si hubieras de amar siempre, sino como quien ha de dejar de amar algún día.”\n - Séneca, Cartas a Lucilio.")
        elif mood == 4:
            print("“El amor es la posibilidad de que alguien te sostenga en el abismo.”\n - Franz Kafka, Cartas a Milena.")
        elif mood == 5:
            print("“Amar es desear para alguien aquello que se considera bueno, por causa de ese alguien y no por causa de uno mismo.”\n - Aristóteles, Ética a Nicómaco.")
    cont = input(f"¿Deseas realizar otra encuesta?(escribe solo si o no en minuscula)\n")
print('''
  _  _____                _                                                 _   _      _                  _ 
 (_)/ ____|              (_)                                               | | (_)    (_)                | |
 | | |  __ _ __ __ _  ___ _  __ _ ___   _ __   ___  _ __   _ __   __ _ _ __| |_ _  ___ _ _ __   __ _ _ __| |
 | | | |_ | '__/ _` |/ __| |/ _` / __| | '_ \ / _ \| '__| | '_ \ / _` | '__| __| |/ __| | '_ \ / _` | '__| |
 | | |__| | | | (_| | (__| | (_| \__ \ | |_) | (_) | |    | |_) | (_| | |  | |_| | (__| | |_) | (_| | |  |_|
 |_|\_____|_|  \__,_|\___|_|\__,_|___/ | .__/ \___/|_|    | .__/ \__,_|_|   \__|_|\___|_| .__/ \__,_|_|  (_)
                                       | |                | |                           | |                 
                                       |_|                |_|                           |_|                 ''')
#Fin del codigo