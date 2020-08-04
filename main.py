
# snake_case
# kebac-case
# camelCase
def day(dia,mes,siglo,ano):
  W = (13 * mes- 1) / 5
  X = ano / 4
  Y = siglo / 4
  Z = W + X + Y + dia + mes - 2 * siglo
  R = Z % 7
  if  R==0:
     return "Domingo"
  elif R==1:
     return "Lunes"
  elif R==2:
     return "Martes"
  elif R==3:
     return "miercoles"
  elif R==4:
     return "jueves"
  elif R==5:
     return "viernes"
  elif R==6:
     return "Sabado"
print day(19,10,20,19)

def triPascal(numero):
        tri=[1]
        x=[0]
        for num in range(max(numero,0)):
          print(tri)
          tri=[o+y for o,y in zip(tri+x,x+tri)]
        return numero>=1
triPascal(10)


vn = input("digito el numero vampiro")
def numerodigito(x):
    numerodigito = 0
    while x != 0:
        digito = x % 10
        if digito != 0:
            numerodigito += 1
        x = x // 10
    return numerodigito
def Par(x):
    if numerodigito(x)%2==0:
        return 1
    else:
        return 0
#
def Ultimo(d):
    ultimocero = 0
    ultimocero= d % 10
    if ultimocero==0:
        return 1
    else:
        return 0

if Par(vn)==1:
    x=[]
    for i in range(int(10**(numerodigito(vn)/2-1)),int(10**(int(numerodigito(vn))/2))):
        x.append(i)
    y=x
    z=0
    px=0
    py=0
    for ai in range(0,len(y)):
        for bi in range(0,len(x)):
            z=y[ai]*x[bi]
            if z==vn and not((Ultimo(x[bi])==1 and Ultimo(y[ai])==1)):
                posiblex=x[bi]
                posibley=y[ai]
                print(vn,"colmillos",px,py)
    if posiblex==0:
        print(vn, "no es vampiro")
else:
    print(vn, "un vampiro")
    