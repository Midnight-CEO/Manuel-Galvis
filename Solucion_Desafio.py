Nombre = str(input("Para ingresar, por favorcoloca tu nombre "))
print("Hola " + Nombre + " Bienvenido a Edutech Solutions")

print ("En esta plataforma te pediremos tus 5 calificaciones para calcular tu promedio y decirte si aprobaste o no el curso")
Calificacion1 = float(input("Coloca tu primera calificacion "))
Calificacion2 = float(input("Coloca tu segunda calificacion "))
Calificacion3 = float(input("Coloca tu tercera calificacion "))
Calificacion4 = float(input("Coloca tu cuarta calificacion "))
Calificacion5 = float(input("Coloca tu quinta calificacion ")) 
Promedio = (Calificacion1 + Calificacion2 + Calificacion3 + Calificacion4 + Calificacion5) / 5
if Promedio >= 60:
    print("Felicidades " + Nombre + " has aprobado el curso con un promedio de " + str(Promedio))
else: 
    if Promedio >= 40 and Promedio <= 59:
        print("Lo siento " + Nombre + " Entraste en el perdiodo de recuperacion del curso con un promedio de " + str(Promedio))
    else: 
        if Promedio < 40 and Promedio >= 0:
            print("Lo siento " + Nombre + " No aprobaste el curso con un promedio de " + str(Promedio))

print("Gracias por utilizar nuestra plataforma " + Nombre + " Esperamos verte pronto en otro curso de Edutech Solutions")