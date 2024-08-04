def factorial():
    numero = int(input('Ingrese un número para darle el resultado factorial del número -> '))
    
    a = 1
    for i in range(numero):
        a *= i+1 
        #print (a)
        print(i)
'''A = 1 
y i = 0 
pero cuando se le suma 1 a i, se convierte en 1, entonces en la primera vuelta seria 1 * 1 = 1
pero en la segunda a igual vale 1 porque la anterior vuelta dio 1, y ahora i también vale 1, entonces 
cuando se le sumé 1, va a valer 2, asi consiguiendo que sea 1 * 2 = 2

ahora el valor de a va a cambiar porque va a ser 2 por el anterior resultado y ahora nuevamente se le suma 1 
a i, y en la tercera vuelta seria 2 * 3 = 6 y asi sucesivamente '''



factorial()