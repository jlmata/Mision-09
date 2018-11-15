#Mision 9: Listas continuacion
# Jose Luis Mata Lomelí
# A01377205


######################################################################

def extraerPares(a):

    pares = []  #Lista vacia
    for i in a:
        if i%2==0:  #Si el numero eliminado es par
            pares.append(i)  #Agregar el numero eliminado a la lista vacia

    return pares


def extraerMayoresPrevios(a):

    MayoresPrevios = []
    for numero in range(1,len(a)):    #Para los numeros dentro de la lista original
        if (a[numero-1] < a[numero]): #Si el numero en x posicion anterior es menor al numero en la posicion
            MayoresPrevios.append(a[numero])    #Agregar el numero de x posicion a la lista vacia si cumple
    return MayoresPrevios

def intercambiarParejas(a):
    z = []
    for numero in range(1,len(a),2):
        z.append(a[numero])
        z.append(a[numero-1])

    if not len(a) % 2 == 0:
        x = len(a) - 1
        z.append(a[x])
    return(z)

def intercambiarMM(a):
    pos_max = 0
    num_max = 0

    pos_min = 0
    num_min = 0

    if len(a) >=2:
        for i in range(0,len(a)):
            if a[i]==max(a):
                pos_max = i
                num_max= a[i]
            if a[i] == min(a):
                pos_min = i
                num_min = a[i]
        a[pos_max] = num_min
        a[pos_min] = num_max
        return a
    else:
        return a



def promediarCentro(a):

    for i in range(0,len(a)):
        if a[i] == max(a) and a[i]==min(a):
            a.remove(max(a))
            a.remove(min(a))

    if len(a) >= 2:
        promedio = sum(a)/len(a)
        return "%.2f" % promedio

def calcularEstadistica(a):
    estadistica = []
    if len(a) >= 2:
        promedio = sum(a)/len(a)

        for i in range(len(a)):
            estadistica.append((a[i]- promedio)**2)
        desviacion = (sum(estadistica)/(len(estadistica)-1))**(1/2)
        return (promedio, desviacion)

    if len(a)==1:
        promedio = sum(a)/len(a)
        return (promedio,0)
    else:
        return (0, 0)



#########################################################################

a = [1,2,3,5,6,8,4]
print(a)

b = extraerPares(a)
print(b)

c = extraerMayoresPrevios(a)
print(c)

d = intercambiarParejas(a)
print(d)

e = intercambiarMM(a)
print(e)

f = promediarCentro(a)
print(f)

g = calcularEstadistica(a)
print(g)

