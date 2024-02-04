a = int(input("Podaj współczynnik a równania: "))
b = int(input("Podaj współczynnik b równania: "))
c = int(input("Podaj współczynnik c równania: "))

#Wzór na deltę= b**2 - 4*a*c 


wybor = int(input("Wybierz działanie: 1.delta 2.pierwiastek z delty 3.miejsce zerowe x1 4.miejsce zerowe x2: "))

if (wybor == 1):
    delta = b**2 - 4*a*c 
    delta > 0 
    print("Twoja delta wynosi: " ,delta)

if (wybor == 2):
    delta = b**2 - 4*a*c 
    pierwiastek = delta **0.5
    print("Pierwiastek z delty wynosi: ",pierwiastek)

elif (wybor == 3):
    delta = b**2 - 4*a*c 
    pierwiastek = delta **0.5
    x1 = -b - pierwiastek / 2*a
    print("Twoje miejsce zerowe x1 wynosi: ", x1)

elif (wybor == 4):
    delta = b**2 - 4*a*c 
    pierwiastek = delta **0.5
    x2 = -b + pierwiastek / 2*a
    print("Twoje zerowe x2 wynosi: ", x2)


