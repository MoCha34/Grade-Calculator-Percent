import random

def studentGennerate():
    student = 1000
    A,B,C,D,F=0,0,0,0,0
    for i in range(student):
        rangrade = graderandom()
        gradetxt = chackgrade(int(rangrade))
        print('Student:',i+1,'point:',rangrade,'grade:',gradetxt)
        if gradetxt is "A":
            A=A+1
        elif gradetxt is "B":
            B+=1
        elif gradetxt is "C":
            C+=1
        elif gradetxt is "D":
            D+=1
        else:
            F+=1          
    print("Percent A:","%.2f"%float((A/1000)*100))
    print("Percent B:","%.2f"%float((B/1000)*100))
    print("Percent C:","%.2f"%float((C/1000)*100))
    print("Percent D:","%.2f"%float((D/1000)*100))
    print("Percent F:","%.2f"%float((F/1000)*100))
    print("Total sum student :",A+B+C+D+F)
def graderandom():
    grade = random.randint(0,100)
    return grade

def chackgrade(g):
      
    if g >= 80:
        return("A")
    elif g>= 70:
        return("B")
    elif g>= 60:
        return("C")
    elif g>= 50:
        return("D")
    else:
        return("F")              


studentGennerate()