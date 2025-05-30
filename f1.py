def sumaHasta(n):
    suma=0
    for i in range(n+1):
        suma+=i
    return suma

def sumaHastaMayor(a, b):
    global vg 
    vg = 2
    if a>=b:
        return sumaHasta(a)
    return(sumaHasta(b))

vg=20
print("sumaHastaMayor(4,3):", sumaHastaMayor(4,3))