dictionary={}
amicable=[]
def d(n):
    temp=1
    Sum=0
    while temp < n :
        if (n % temp == 0):
            Sum+=temp
        temp+=1
    return Sum
    
        
            
n=1
while n < 10000:
    k=d(n)
    dictionary[n]=k
    n=n+1

#print dictionary

for i , j in dictionary.items():
    if(i!=j):
        for m in dictionary.keys():
            if ( j==m and i==dictionary[m] ):
                amicable.append(i)
                
            
print amicable
print sum(amicable)
