import random
import math
#1.
täisarvud=0
for i in range(15):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1} arv:"))
            break
        except:
            print("Kirjuta ainult numbrid")
    if arv==int(arv): täisarvud+=1
print(f"Täisarvude kogus: {täisarvud}")


#2
summ=0
while True:
    try:
        A=int(input("Sisesata A:"))
        if A>1:
            for i in range (1,A+1):
                summ+=i
            print(f"Summa võrdub {summ}-ga")
            break
        else:
            print("Arv A peab olla rohkem kui 1")
    except:
        print("Vale formaat")



#3
kor=1
for i in range (8):
    while True:
        try:
            a=float(input(f"Sisesta {i+1} arv:"))
            if a>0:
              kor*=a
              break
            else:
                print("Arv A peab olla rohkem kui 0")  
        except:
            print("Vale formaat")
print(f"Korrutamine võrdub {kor}-ga")
            


#5
summ=0
while True:
    try:
        N=int(input("Sisesata N:"))
        if N>1:
            for i in range (1,N+1):
                arv=float(input(f"Sisesta {i} arv:"))
                if arv<0:
                    summ+=arv
            print(f"Summa võrdub {summ}-ga")
            break
        else:
            print("Arv A peab olla rohkem kui 1")
    except:
        print("Vale formaat")

#4
for i in range (10,21,1):
    try:
        print(f"Number ruutu {i} võrdub {i**2}")
    except: 
        print("Vale formaat")

#15
for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()


#6
positiivsed=0
negatiivsed=0
nuul=0
while True:
    try:
        N=int(input("Sisesata N:"))
        if N>1:
            for i in range (1, N+1):
                arv=float(input(f"Sisesta {i} arv:"))
                if arv>0:
                    positiivsed+=1
                elif arv<0:
                    negatiivsed+=1
                else:
                    nuul+=1 
            break
    except:
       print("Vale formaat")
print (f"Positiivseid arve: {positiivsed}")
print(f"Negatiivseid arve: {negatiivsed}")
print(f"Nulle: {nuul}")

#7
K=int(input("Sisesta K:"))
A=int(input("Sisesata A:"))
B=int(input("Sisesata B:"))
try:
    if A>0 and B>0:
        for i in range (A, B+1):
            if i%K==0:
                print(i)
            else: 
                print("A ja B peavad olema positiivsed ja A peab olema väiksem või võrdne B-ga!")

except: 
      print("Vale formaat")


#10
for j in range(10):
    a1=float(input("Esimene arv: "))
    a2=float(input("Teine arv: "))
    if a1>a2:
        print(f"Suurem on {a1}")
    elif a2>a1:
        print(f"Suurem on {a2}")

#9
print("Sentimeetrid / Inch ")
print("--------------------")

for i in range(1,21):
    print (f"{i}              {i*2.5 }", end=" ")
    print( )

#11
summ=0
kogus=int(input("Sisesta kogus: "))
arv=int(input("Sisesta arv: "))
try:
    for i in range (kogus):
        arv_=int(input(f"Sisesta {i+1} arv: "))
        if arv_>= 10 and arv_<100:
                if arv_%2==0 and arv_%arv==0:
                    summ+=arv_
        else:
            print("Sisesta arv, et suurem kui 10.")
except: 
    print("Vale formaat")
print(f"Arvude summa on: {summ}")

#13
summ=0
for i in range (100,1001):
    if i%7==0:
        summ+=i
print(f"Arvude summa on: {summ}")

#14
kor=1
try:
    N=random.randint(1, 100)
    for i in range (1, N):
        kor*=i
except: 
    print("Vale formaat!")
print(f"Korrutamine alates 1 kuni {N}")
print(f"Korrutamine võrdub {kor}-ga")

#17
try:
    for i in range(9):
        print(2,"*",i+1, "=", 2*(i+1),"\n", end=" ")
    print()
except:
    print("Vale formaat")

#18
try:
    for i in range (20, 51):
        if i%3==0 and i%5!=0:
            print(i)
except: 
    print("Vale formaat")

#20
try:
    for i in range (1, 51):
        if i%5==0 or i%7==0:
            print(i)
except:
    print("Vale formaat")


#21
arv=0
try:
    for i in range(10):
        arv=int(input(f"Sisesta {i+1} arv: "))
        if arv<0:
            arv = -arv
        print(arv)
except:
    print("Vale formaat")



#22
summ=0
try:
    for i in range(100,201):
        if i%17==0:
            summ+=i
except:
    print("Vale formaat")
print(f"Arvude summa on: {summ}")

#25
k=0
try:
    N=int(input("Sisesta N: "))
    for i in range (N):
        if i%2!=0 and i%3!=0 and i%5!=0:
            k+=1
except:
    print("Vale formaat")
print (k)

#28
p=0
arv= random.randint(1, 100)
print("Tere tulemast mini loterii! Arva ära number (1 kuni 100):")
while True:
    try:
        a = int(input("Sisesta oma pakkumine: "))  
        p += 1
        if a>arv:
            print("Liiga väike, proovi uuesti.")
        elif a<arv:
            print("Liiga suur, proovi uuesti.")
        else:
            print(f"Õnnitleme! Arvasid numbri {arv} ära {p} katsega.")
            break  
    except:
        print("Vale formaat")