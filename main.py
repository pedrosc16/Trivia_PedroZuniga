from random import randint
import time

attempt = 1
run_program = True
name = ""
puntaje_inicial = randint(1, 30)
puntaje_final = 0
get_points = []
negative_number = 0
positive_number = 0
correct_answers = [10, 20, 30]
incorrect_answers = [6, 5, 5]
options = ['a', 'b', 'c', 'd']


#Una clase que te brinde los colores
class colors:
    white = '\033[1;37m'
    yellow = "\033[1;33m"
    green = "\033[1;32m"
    blue = "\033[1;34m"
    cyan = "\033[1;36m"
    red = "\033[1;31m"
    magenta = "\033[1;35m"
    black = "\033[1;30m"
    darkwhite = "\033[0;37m"
    darkyellow = "\033[0;33m"
    darkgreen = "\033[0;32m"
    darkblue = "\033[0;34m"
    darkcyan = "\033[0;36m"
    darkred = "\033[0;31m"
    darkmagenta = "\033[0;35m"
    ENDC = "\033[m"


#Para colocar el nombre de manera correcta con una mayuscula inicial
def correct_name(name):
    return name.capitalize()


#Definir una funcion que brinde los tiempos de espera
def wait(tiempo):
    time.sleep(tiempo)


while run_program == True:

    print(colors.darkcyan +
          "\n     ******Bienvenido Futuro Desarrollador Backend*******   " +
          colors.ENDC)

    wait(0.8)
    print(
        "\nHola amante del software y del hardware pero sobre todo de la tecnologia , me parece que estoy en lo cierto ya que te gusta todo lo relacionado a la programacion, el dia de hoy tengo ganas de retarte, por lo cual quiero que me demuestres tus conocimientos ."
    )
    wait(2)
    if attempt==1:
      name=input("\nPero antes de ello brindame tu Nombre por favor : ")
    print(
        "\nHola " + correct_name(name) +
        " por lo visto este es tu intento numero :", attempt)
    wait(1)
    print("\nMuchas gracias " + correct_name(name) +
          " ahora prosigamos con el reto aceptas ? ")
    try:
        value_one = int(input("\nColoca 1 para 'SI' o coloca 2 para 'NO' : "))
    except ValueError:
        value_one = int(
            input(
                "\nNo escribas otro caracter ...Coloca 1 para 'SI' o coloca 2 para 'NO' : "
            ))

    while (value_one != 1 and value_one != 2):
        value_int = int(
            input(
                "\nNo coloques otro valor ...Coloca 1 para 'SI' o coloca 2 para 'NO' : "
            ))

    if value_one == 1:
        input(
            "\nPerfecto " + correct_name(name) +
            " eres un joven de retos continuemos....Presiona Enter para proseguir"
        )

    elif value_one == 2:
        input(
            '\nDe verdad ' + correct_name(name) +
            ' creias que te iba a dar oportunidad de salirte , pues no ahora , si aun ni empezamos , asi que prosigamos...Presiona Enter'
        )

    input(
        "\nProcederé a explicar las instrucciones , habran 10 preguntas  entre las cuales cada una de ellas tendra solo una alternativa correcta, sin embargo habran niveles de preguntas que difieren a traves del color :Facil (Amarillo),  Intermedio(Verde), Dificil(Rojo).....Presiona Enter para continuar"
    )

    input(
        "\nRecordar tambien que por cada respuesta correcta se te brindaran 10 puntos en las faciles , 20 en las intermedias y 30 en las dificiles, asi como cuando falles en alguna pregunta se reduciran tus puntos  6 puntos en las faciles 5 en intermedia y 5 en las dificiles , con lo cual de manera regular  en el mejor de los casos tu puntaje podria ser 180....Presiona enter para proseguir"
    )

    print(
        colors.red +
        "\n!Sin embargo te encontraras con algunas sorpresas en el camino que hara de esta trivia mas divertida y a la vez incierta con respecto a los puntos que podras alcanzar! "
        + colors.ENDC)
    wait(2)
    input(
        "\nBien ahora se desglosaran las preguntas , en las cuales pondras a prueba tus conocimientos de joven y futuro desarrollador. !Mucha suerte! ....Presiona Enter para empezar con la trivia "
    )
    input(
        " \nPero Espera!!! Como deseo ayudarte " + correct_name(name) +
        " te asignare un puntaje del 1 al 30 para iniciar , si! , lo que entendiste "
        + correct_name(name) +
        " es decir te otorgare algo de puntaje sin siquiera haber iniciado la trivia ,aprovechalo ! ... Presiona Enter para saber que puntaje se te otorgo"
    )

    print("\nTu puntaje inicial es :", puntaje_inicial)
    wait(1)
    if puntaje_inicial <= 10:
        input(
            "\nMmmm " + correct_name(name) +
            " pudiste haber tenido algo de mejor suerte pero no esta mal  ahora si prosigamos a las preguntas...Presiona Enter ahora si para ir a la trivia"
        )

    elif puntaje_inicial > 10 and puntaje_inicial <= 20:
        input(
            "\nBien " + correct_name(name) +
            " sacaste un puntaje bueno para empezar ahora si prosigamos a las preguntas......Presiona Enter ahora si para ir a la trivia "
        )

    else:
        input(
            "\nExcelente " + correct_name(name) +
            " parece ser tu dia de suerte el puntaje que ganaste es mayor al promedio  ahora si prosigamos a las preguntas......Presiona Enter ahora si para ir a la trivia "
        )

    print(colors.blue + "\n***********Trivia Geek***************")
    wait(1)
    print(
        colors.yellow +
        "\nPregunta 1) ¿Cual de estos componentes no es fundamental para la computadora"
    )
    print("\na)Memoria Ram\nb)Procesador\nc)Camara Web\nd)Disco duro" +
          colors.ENDC)
    wait(1)
    answer1 = input("\nColoque la respuesta correcta a , b , c , d : ")
    while answer1 not in options:
        answer1 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer1 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer1 == 'b':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer1 == 'c':
        print(
            "\nUn ordenador puede funcionar tranquilamente sin una camara web con lo cual no es indispensable para su funcionalidad"
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[0], "puntos")
        get_points.append(correct_answers[0])

    elif answer1 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(
        colors.yellow +
        "\nPregunta 2) ¿Cual es el sistema operativo mas usado en los ordenadores"
    )
    print("\na)Linux\nb)Windows\nc)Debian\nd)Ubuntu" + colors.ENDC)
    wait(1)
    answer2 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer2 not in options:
        answer2 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer2 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer2 == 'b':
        print(
            "\nSegun las estadisticas, Windows hasta el año 2021 lleva instalado su S.O en el 74.76'%' de las computadoras del mercado "
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[0], "puntos")
        get_points.append(correct_answers[0])

    elif answer2 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer2 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(colors.yellow + "\nPregunta 3) ¿Quien fue el fundador de Microsoft?")
    print(
        "\na)Marck Zuckerberg\nb)Bill Gates\nc)Stephen Hawking\nd)Elon Musk" +
        colors.ENDC)
    wait(1)
    answer3 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer3 not in options:
        answer3 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer3 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer3 == 'b':
        print(
            "\nEn abril de 1975, con 20 años de edad, Bill Gates, hijo de un destacado abogado y de una profesora de la Universidad de Washington, fundó, junto a Paul Allen, Microsoft"
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[0], "puntos")
        get_points.append(correct_answers[0])

    elif answer3 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer3 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    input(
        colors.blue +
        "\nOh! Espera!  al parecer es tu dia de suerte o de mala suerte , depende como lo veamos , te has topado con una pregunta secreta la cual te da la posibilidad de aumentar tus puntos exageradamente o disminuirla exageradamente tambien , asi que ten mucho cuidado con la siguiente pregunta secreta"
    )

    print(
        "\nPregunta Secreta) ¿Como se llamaba la primera computadora inventada"
    )
    print("\na)Raspberry pi\nb)APPLE II\nc)ENIAC\nd)UNIVAC" + colors.ENDC)
    wait(1)
    answer_secret = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer_secret not in options:
        answer_secret = input(
            "\nColoque la respuesta correcta a , b , c , d : ")

    if answer_secret == 'a':
        print(
            "\nLa respuesta es incorrecta y esta respuesta era imposible , debido a que esta es una pregunta secreta te descontare la mitad de tus puntos..ten mucho cuidado para la proxima quizas haya otra pregunta secreta por ahi  te voy a restar tus puntos por la mitad , si es impar sera un poco mas de la mitad y si es negativo se duplicara"
        )
        wait(1)
        if (puntaje_final % 2 == 0 and puntaje_final > 0):
            print("\nCon lo cual se  va a reducir el puntaje en ",
                  puntaje_final / 2)
            get_points.append(int(-puntaje_final / 2))
        elif (puntaje_final % 2 != 0 and puntaje_final > 0):
            print("\nCon lo cual se  va a reducir el puntaje en ",
                  (puntaje_final + 1) / 2)
            get_points.append(int(-(puntaje_final + 1) / 2))

        else:
            print("\nCon lo cual se  va a duplicar tu puntaje disminuyendo ",
                  (puntaje_final))
            get_points.append(int(-puntaje_final * 2))

    elif answer_secret == 'b':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran 10 puntos ya que al ser una respuesta secreta el puntaje que pierdes y el riesgo es mayor"
        )
        get_points.append(-10)

    elif answer_secret == 'c':
        print(
            "\nEn 1943, se inició la construcción del primer ordenador de propósito general basado en circuitos electrónicos, el ENIAC (acrónimo de Electronic Numerical Integrator And Computer). El ENIAC se terminó de construir en 1945 y se presentó al público el 15 de febrero de 1946."
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual al ser una pregunta secreta te voy a brindar 40 puntos adicionales!, si asi como lo ves , se te sumaran 40 puntos"
        )
        get_points.append(40)

    elif answer_secret == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran 10 puntos ya que al ser una respuesta secreta el puntaje que pierdes y el riesgo es mayor"
        )
        get_points.append(-10)

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(
        colors.yellow +
        "\nPregunta 4) ¿Cual dispositivo de la computadora permite la funcion de dar click , señalar , arrastrar o seleccionar"
    )
    print("\na)Teclado\nb)Usb\nc)Mouse\nd)Monitor" + colors.ENDC)
    wait(1)
    answer4 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer4 not in options:
        answer4 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer4 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer4 == 'b':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    elif answer4 == 'c':
        print(
            "\nEl mouse es el unico componente del ordenador el cual permite arrastar , dar click"
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[0], "puntos")
        get_points.append(correct_answers[0])

    elif answer4 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[0])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")
    input(
        colors.green +
        "\nAhora pasaremos a la seccion de las preguntas Intermedias, preparate....Enter para continuar"
    )

    print(
        "\nPregunta 5) Una marca reconocida de ordenadores y laptops se llama HP , que significado tiene estas siglas?"
    )
    print(
        "\na)Hire Purchase\nb)Hewlett Packard\nc)Horse Power\nd)Health Points"
        + colors.ENDC)
    wait(1)
    answer5 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer5 not in options:
        answer5 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer5 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer5 == 'b':
        print(
            "\nHewlett-Packard o HP, es una de las mayores e importantes empresas de tecnologías de la información del mundo. Fabrica y comercializa hardware y software además brinda servicios de asistencia relacionados con la informática."
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[1], "puntos")
        get_points.append(correct_answers[1])

    elif answer5 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer5 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[0], "puntos")
        get_points.append(-incorrect_answers[1])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(
        colors.green +
        "\nPregunta 6)¿En que año se empezo a desarrollar el sistema operativo Android?"
    )
    print("\na)2000\nb)2001\nc)2002\nd)2003" + colors.ENDC)
    wait(1)
    answer6 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer6 not in options:
        answer6 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer6 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer6 == 'b':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer6 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer6 == 'd':
        print(
            "\nAndroid nació en el año 2003 de la mano de Rich Miner, Nick Sears, Chris White y Andy Rubin. Este grupo tenía la intención de crear dispositivos móviles que fueran más conscientes de la localización y las preferencias de los usuarios. Los comienzos de Android, totalmente en secreto, no fueron sencillos."
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[1], "puntos")
        get_points.append(correct_answers[1])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(colors.green + "\nPregunta 7)¿1 byte a cuantos bits equivale?")
    print("\na)4 bits\nb)8 bits\nc)16 bits\nd)24 bits" + colors.ENDC)
    wait(1)
    answer7 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer7 not in options:
        answer7 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer7 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer7 == 'b':
        print("\nUn byte equivale a un conjunto ordenado de 8 bits. ")
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[1], "puntos")
        get_points.append(correct_answers[1])

    elif answer7 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer7 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(colors.green +
          "\nPregunta 8)¿En que año fue lanzado el primer iphone?")
    print("\na)2002\nb)2007\nc)2004\nd)2000" + colors.ENDC)
    wait(1)
    answer8 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer8 not in options:
        answer8 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer8 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer8 == 'b':
        print(
            "\nEl 29 de junio de 2007 Apple dio uno de los pasos más importantes de su historia saco el primer iphone al mercado"
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[1], "puntos")
        get_points.append(correct_answers[1])

    elif answer8 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    elif answer8 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[1], "puntos")
        get_points.append(-incorrect_answers[1])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")
    input(
        colors.red +
        "\nAhora procederemos a pasar a las preguntas mas dificiles , listo?...Enter para continuar"
    )

    print(
        "\nPregunta 9)¿Cual fue el primer nombre de la primera computadora de IBM?"
    )
    print("\na)IBM 4310\nb)IBM 5150\nc)MACINTOSH\nd)IBM 3720" + colors.ENDC)
    wait(1)
    answer9 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer9 not in options:
        answer9 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer9 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[2], "puntos")
        get_points.append(-incorrect_answers[2])

    elif answer9 == 'b':
        print(
            "\nEl IBM Personal Computer, conocido comúnmente como IBM PC, fue la versión original y el progenitor de la plataforma de hardware compatible IBM PC. Es el IBM modelo 5150, y fue introducido el 12 de agosto de 1981 haciendo parte de la quinta generación de computadoras"
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[2], "puntos")
        get_points.append(correct_answers[2])

    elif answer9 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[2], "puntos")
        get_points.append(-incorrect_answers[2])

    elif answer9 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[2], "puntos")
        get_points.append(-incorrect_answers[2])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nTu puntaje actual es ", puntaje_final, "puntos")
    wait(1)
    input("Presione enter para proseguir a la siguiente pregunta....")

    print(colors.red +
          "\nPregunta 10)¿Como se llama el primer programador de la historia?")
    print(
        "\na)Charles Babbage\nb)Ada Lovelace\nc)Alan Turing\nd)Linus Torvalds"
        + colors.ENDC)
    wait(1)
    answer10 = input("\nColoque la respuesta correcta a , b , c , d : ")

    while answer10 not in options:
        answer10 = input("\nColoque la respuesta correcta a , b , c , d : ")

    if answer10 == 'a':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[2], "puntos")
        get_points.append(-incorrect_answers[2])

    elif answer10 == 'b':
        print(
            "\nAda Lovelace fue la primera programadora de la historia. Matemática y escritora inglesa, hija del famoso poeta Lord Byron"
        )
        print(
            "\nExcelente! la respuesta es correcta con lo cual se te sumaran ",
            correct_answers[2], "puntos")
        get_points.append(correct_answers[2])

    elif answer10 == 'c':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[2], "puntos")
        get_points.append(-incorrect_answers[2])

    elif answer10 == 'd':
        print(
            "\nLo siento la respuesta es incorrecta con lo cual se te restaran ",
            incorrect_answers[2], "puntos")
        get_points.append(-incorrect_answers[2])

    puntaje_final = puntaje_inicial + sum(get_points)
    print("\nBueno " + correct_name(name) + " tu puntaje final es ",
          puntaje_final, "puntos")
    wait(1)
    print(
        "\nAqui te dejo los puntajes que fuiste ganando o perdiendo en el transcurso del juego para que tu mismo saques tus calculos son : ",
        end="")
    for i in get_points:
        print(i, end=",")
    print("")

    for y in range(len(get_points)):
        if (get_points[y] > 0):
            positive_number = positive_number + 1

        elif (get_points[y] < 0):
            negative_number = negative_number + 1

    print("\ntuviste ", positive_number, "respuestas correctas")
    print("\ntuviste ", negative_number, "respuestas incorrectas")
    wait(1)
    print(colors.blue + "\nDime " + correct_name(name) +
          " deseas volver a jugar la trivia ?")
    wait(1)
    repeat = input(
        "\nIngrese 'si' si deseas repetir el juego, en caso contrario que ya no desees jugar ingresa 'no' : "
        + colors.ENDC)
    while repeat not in ('no', 'si'):
        repeat = input(
            "\nIngrese 'si' si deseas repetir el juego, en caso contrario que ya no desees jugar ingresa 'no' : "
        )

    if (repeat == 'no'):

        break
    elif (repeat == 'si'):
        attempt = attempt + 1
        puntaje_final = 0
        get_points.clear()
        puntaje_inicial = randint(1, 30)
        negative_number = 0
        positive_number = 0
    else:

        break

print(
    "\nEspero que te hayas divertido , muchas gracias " + correct_name(name) +
    " por haberte pasado aqui , espero volverte a ver pronto . Suerte en la preseleccion! :)"
)
