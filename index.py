daño = 0
vida = 100
print("GUARDIAN TALES")
inicio = input("Escribe enter para entrar(Si no quieres pon Tung Tung Tung Tung Tung Tung Tung Saur) ")
if inicio == "enter":
    print("*Musiquita*")
    continuar = True
elif inicio == "Tung Tung Tung Tung Tung Tung Tung Saur":
   print(f"Never gonna give you up, never gonna let you down\n"
      "Never gonna run around and desert you\n"
      "Never gonna make you cry, never gonna say goodbye\n"
      "Never gonna tell a lie and hurt you")
   continuar = "Trol"
else:
    print("._. Ah")
    continuar = False
if continuar == "Trol":
    print("En un rincón olvidado de los vastos desiertos del Tiempo, se cuenta la leyenda de Tung Tung Saur, el Guardián del Eco Eterno. Nacido de un trueno que jamás dejó de resonar, Tung Tung Saur vaga por los límites de la realidad, despertando a los soñadores con su tambor de madera ancestral. Cuenta la historia que Tung Tung Saur aparece en las noches más silenciosas, cuando el viento se detiene y las estrellas parpadean con inquietud. Con cada (Tung Tung Tung), el aire vibra y las sombras tiemblan. Los ancianos narran que no es un simple sonido, sino un eco atrapado entre dimensiones, una advertencia para aquellos que han olvidado sus sueños más profundos. Nadie sabe exactamente cómo luce Tung Tung Saur. Algunos dicen que es una figura alta y delgada, con brazos largos que se extienden como ramas, mientras que otros aseguran haber visto un ente hecho de madera petrificada, con ojos incandescentes que brillan al ritmo de sus golpes. Sin embargo, todos coinciden en algo: su presencia es imposible de ignorar. Los más valientes han intentado seguir el sonido, adentrándose en bosques oscuros y ruinas antiguas. Aquellos que lograron regresar cuentan historias de espejos que reflejan paisajes imposibles y puertas que conducen a lugares que no deberían existir. (Seguir a Tung Tung Saur es caminar entre los ecos del pasado y los susurros del futuro), murmuran en voz baja los que volvieron. cada año, durante la luna más brillante del otoño, los pueblos cercanos realizan un ritual para honrar su presencia. Se tocan tambores en las plazas, los niños pintan máscaras de madera, y las leyendas se narran al calor de las fogatas. (Escucha el Tung Tung Tung en la noche y recuerda quién eres), dicen los más sabios. Porque en el eco de Tung Tung Saur no solo resuena un tambor, sino la voz de un tiempo olvidado, un recordatorio de que los sueños, aunque sepultados por el peso de los días, jamás dejan de latir.")
if continuar == True:
    print("*Una mariposa revolotea por lo largo de un tranquilo y bello reino*")
    print("*A lo lejos se ven unos caballeros entrenando*")
    print("Eva(Capitana de caballeria): Muy bien hecho novatos, recuerden que tenemos que darlo todo para protger el reino de Kanterbury")
    print("Eva: Ey tu, el de ahi, el que juega lol(Si, tu wey, no te hagas)")
    print("Eva: ¿Como te llamas?")
    nombre = input()
    print(f"Eva: Que carita mas tontuna tienes {nombre}")
    print("*Se escucha una explosion y el reino entero empieza a temblar*")
    print("Eva: ¿Que esta pasando?")
    print("*Explota donde nuestro prota estaba entrenando y cae al vacio (Estan entrenando en una torrecita)")
    print("*Por la explocion perdiste la conciencia, y al despertar te das cuenta que una extraña chica te ha salvado de morir por la caida")
    print(f"La chica misteriosa: Es bueno volver a verte {nombre}")
    sapo = input("Quieres sapear al nuevo personaje (1.Si  2.No) ")
    if sapo == "1":
        print("Es una chica joven con el pelo color rubio, se le ve una expresion triste, ocupa una armadura y una guadaña de luz, tal parece que maneja la luz")
    else:
        print("Weno, weno")
    print("*Luego de caer en la superficie, la chica desaparece*")        
    print("*Encuentras una espada muy fea, pero no tienes arma para defenderte*")
    print(f"Tus stats iniciales son:\n"
          "Vida = 100 \n"
          "Ataque = 0 \n"
          "Defensa = Reduccion del 25%")
    recoger = input("¿La agarras? (1.Si 2.No) ")
    if recoger == "1":
        print("Bien hecho, ahora tu daño es = 30")
        daño += 30
    else: 
        print("OK, ya veras como sobrevives")
        recoger_1 = input("Seguro que no la quieres recoger (1.Si 2.No) ")
        if recoger_1 == "2":
            print("Tons, la recoges??????")
            recoger_2 = input("1.SI 2.Si 3.Sipirli ")
            if recoger_2 == "1" or recoger_2 == "2" or recoger_2 == "3":
                print("Very gud, continuemos.....")
                print("Ah, si. +30 de daño")
                daño += 30
        else:
            print(">:(")
            print("Te quedas sin arma y tu daño no aumenta")
            daño = 0
    print("Tras avanzar te encuentras con un extraño ser oscuro, tambien tiene un casco y tiene unas marcas rojas")
    print("El enemigo tiene 20 de vida y 100 de daño")
    ataque = input("1.ATACAR 2.DEFENDER 3.XD" )
    if ataque == "1" and recoger == "1":
        print("*Le quitas 30 de vida")
        print("Se murio UwU")
    elif ataque == "2" and daño == 0:
        print("Te moriste waton :()")
        continuar = False
        print("FIN DEL JUEGO")
    elif ataque == "3":
        print("Tu y el ser invasor del reino se besan apasionadamente, que momento mas romantico, pero..... te deja pasae sin problemas y te regala un arma")
        daño = 1000
    if continuar == True:
        print("Despues de ver todo el caos en el que se ve afectado tu reino, tu corazon se llena de determincion")
        print("Es hora de ir a ver a la reina Camile y a su hermanita la princesita")
        print("Camino al castillo te encuentras con un extraño ser, mucho mas que el anterior")
        print("Este nuevo ser parece ser un insecto gigante, tiene una masa verde en su parte infeior")
        print("Es hora de luchar por el reino")
        print("POR KANTERBURY")
        print("Datos del monstruo: Vida = 60  Ataque = 50")
        vida_monstruo = 60
        atack = input(f"Que haras para salvar tu reino {nombre} (1.Atacar 2.Actuar) ")
        if atack == "1":
            life = vida_monstruo - daño
            print("*Le haces un ataque tajante*")
            if life <=0:
                print("Lo mataste, esoooo")
                print("Y de un solo golpe")
                continuar = True
            elif life == 30:
                print("Le has quitado 30 de vida y le quedan 30")
                print("El monstruo ataca")
                print("Vida tuya restante = 50")
                vida = 50
                movimiento = input("Que haras ahora? (1.Atacar 2.Actuar) ")
                if movimiento == "1":
                    print("Un ataque efectivo que mata al enemigo, muy bien :D")
                    continuar = True
                if movimiento == "2":
                    print("Le dices al monstruo que puede haber otra solucion y le cantaas")
                    print("Parece que funciona pero ataca")
                    print("Te moriste ;-;")
                    continuar = False
                    print("FIN DEL JUEGO")
        if atack == "2":
            print("Le cantas Chayanne al monstruo y parece mas calmado")
            print("Aun asi ataca, pero tal vez se calme si lo intentas una vez mas")
            print("Tu vida restante = 50")
            movimiento = input("Que haras ahora? (1.Atacar 2.Actuar) ")
            if movimiento == "1":
                print("When: Lo dejaste a 30, muy bien")
                print("But: Te ataco y te moriste")
                print("FIN DEL JUEGO")
                continuar = False
            if movimiento == "2":
                print(f"Puedes desafiarte\n"
                    "Y errores enmendar\n"
                    "Puedes renovarte\n"
                    "¡No hay que batallar!\n")
                print("OMG, Ahora es bueno")
                print("Nueva mascota")
                mascota = True
                continuar = True
    if continuar == True:
        print("Es hora de entrar al castillo")
        if mascota == True:
            print("Tu mascota se tendra que quedarse afuera, te da un silbato para cuando quieras llamrlo")
        print("*Al entrar ves a la reina Camile y a la princesita junto a Eva*")
        print("*Te acercas lentamente y la princesita va corriendo a abrazarte*")
        print("*La oscuridad se cierne sobre el castillo*")
        print("Camile: No podemos seguir aca, he evacuado a todo el reino, ahora nos toca a nosotros")
        print("*La reina Camile ocupa su poder y salen del reino volando*")
        print("*Un ser oscuro se acerca volando*")
        print("*Han deribado a Eva*")
        print("La princesita: Han derribado a Eva, nooooooo ;-;")
        print("Camile: No te preocupes hermanita, estara bien")
        print("*Tu y la princesita son derribados*")
        print("La princesita: Hermana, nooooo")
        print("Camile: Hermanitaaaa")
        print("*Ven como la Reina Camile igual es atacada*")
        print("*Con su ultimo aliento, la Reina Camile te dice*")
        print("As de los guardianes, por favor protege a mi hermanita")
        print("*Abrazas a la princesita para que juntos puedan amortiguar la caida en un lago cercano*")
        print("*Despues de la caida quedan inconscientes, pero vivos*")
        print("Despiertas y ya no esta la princesita")
        print(f"{nombre}: Debo encontrar a la princesita")
        print("CONTINUARA")