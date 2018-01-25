import math
izbor=1
def passeeeee():
    try:
        return 0
    except:
        if True:
            pass
while izbor>=1 and izbor<=6:
    print("Kalkulator:")
    print("1.zbrajanje")
    print("2.oduzimanje")
    print("3.dijeljenje")
    print("4.množenje")
    print("5.korjenovanje")
    print("6.potenciranje")
    izbor=int(input("Koju operaciju želiš provesti!?"))

    if izbor==1:
        izbor1=True
        a=float(input("Unesi broj:"))
        suma=a
        while izbor1:
            b=float(input("Unesi broj:"))
            suma=suma+b
            novi_broj=input("Želiš li zbrojiti još brojeva od " +str(suma)+" , da ili ne:")
            if novi_broj=="da":
                pass
            else:
                izbor1=False
        print("Zbroj unesenih brojeva iznosi",suma)
        dalje=input("Pritisni ENTER za dalje:")

    elif izbor==2:
        izbor2=True
        a=float(input("Unesi umanjenik:"))
        razlika=a
        while izbor2:
            b=float(input("Unesi umanjitelj:"))
            razlika=razlika-b
            novi_broj=input("Želiš li oduzeti još brojeva od "+str(razlika)+ " , da ili ne:")
            if novi_broj=="da":
                pass
            else:
                izbor2=False
        print("Razlika unesenih brojeva iznosi:",razlika)
        dalje = input("Pritisni ENTER za dalje:")

    elif izbor==3:
        izbor3=True
        a=float(input("Unesi djeljenik:"))
        kolicnik=a
        while izbor3:
            b=float(input("Unesi djeljitelj:"))
            if(b==0):
                print("Dijeljenje s nulom")
                continue
            else:
                kolicnik=kolicnik/b
            novi_broj=input("Želiš li podjeliti "+str(kolicnik)+" s novim brojem, da ili ne:")
            if novi_broj=="da":
                pass
            else:
                izbor3=False
        print("Količnik unesenih brojeva iznosi",kolicnik)
        dalje = input("Pritisni ENTER za dalje:")

    elif izbor==4:
        izbor4=True
        a=float(input("unesi faktor:"))
        umnozak=a
        while izbor4:
            b=float(input("unesi faktor:"))
            umnozak=umnozak*b
            novi_broj=input("Želiš li pomnožiti "+str(umnozak)+" s novim brojem,da ili ne:")
            if novi_broj=="da":
                pass
            else:
                izbor4=False
        print("Umnožak unesenih brojeva iznosi",umnozak)
        dalje = input("Pritisni ENTER za dalje:")

    elif izbor==5:
        a=float(input("Unesi broj:"))
        print("Korijen broja "+str(a)+" iznosi:",math.sqrt(a))
        dalje = input("Pritisni ENTER za dalje:")

    elif izbor==6:
        a=float(input("Unesi broj koji potenciramo:"))
        b=int(input("Unesi potenciju:"))
        print(str(b)+". potencija broja "+str(a)+" iznosi",pow(a,b))
        dalje = input("Pritisni ENTER za dalje:")
