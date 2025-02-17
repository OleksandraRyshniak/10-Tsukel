1.
täisarvud=0
for i in range(15):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1} arv:"))
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



3
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
            


5
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

4
for i in range (10,21,1):
        print(f"Number ruutu {i} võrdub {i**2}")

#15
for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()


6
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
arv=0
while True:
    try:
        A=int(input("Sisesata A:"))
        B=int(input("Sisesata B:"))
        if A>1 and B>1:
            for i in range (A, B+1):
                arv=float(input(f"Sisesta {i} arv:"))
            if arv

#10
for j in range(10):
    a1=float(input("Esimene arv: "))
    a2=float(input("Teine arv: "))
    if a1>a2:
        print(f"Suurem on {a1}")
    elif a2>a1:
        print(f"Suurem on {a2}")
        

        gk