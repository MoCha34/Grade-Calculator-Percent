import random

def studentGennerate():
    student = 1000
    for i in range(student):
        rangrade = graderandom()
        print('Student:',i+1,'grade is :',rangrade)

def graderandom():
    grade = random.randint(0,100)
    return grade
    #print(grade)

def chackgrade():
    g = int()
    if g >= 80:
        print("A")
    elif g>= 70:
        print("B")
    elif g>= 60:
        print("C")
    elif g>= 50:
        print("D")
    else:
        print("F")              

def gradepercent():
    print("")        

