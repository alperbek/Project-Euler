maxD={} 
counter=0
def Collatz(num):
    global counter
    if(num != 1):
        if(num % 2 == 0):
            counter+=1
            num = num/2
            return Collatz(num)
        else :
            counter+=1
            num = 3 * num +1
            return Collatz(num)
    else :
        counter+=1
        return counter
num=13
while num < 1000000:
    c=Collatz(num)
    maxD[num]=c
    num=num+1
    counter=0

liste=maxD.values()
Max=max(liste)

for i,j in maxD.items():
    if ( j == Max ):
        print "{} : {}".format(i,j)
