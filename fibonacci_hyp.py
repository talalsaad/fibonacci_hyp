import math
bits=5
counter=0
arr=[]
arrb=[]
state=True
sum=0;


def d(n):
    x=bin(n).replace("0b", "");
    while len(x) < bits:
        x= '0'+x
    return x

    
def eu(x):
    if(x<=0):
        return 0;
    elif (x==1):
        return 1;
    elif (x==2):
        return 3;
    return eu(x-1)+eu(x-2)+fu(x+2)-1; 
def fu(x):
    if(x<=0):
        return 0;
    elif (x<=2):
        return 1;
    return fu(x-1)+fu(x-2);

while(state):
    for x in range(bits-1):
        if(int(d(counter)[x])+int(d(counter)[x+1])==2):
            break
        if(x==bits-2):
            arr.append(counter)
    if(len(arr)==fu(bits+2)):
        state=False
    counter=counter+1



for x in(arr):
    arrb.append(d(x))
print("Level:",bits)
print("Longest deistens:",math.ceil(bits/2))
print("Average deistens:",fu(bits+2)/(fu(bits+2)-1))
print("Values in decimal:",arr)
print("Values in binary:",arrb)
print("Number of nodes:",fu(bits+2))
print("Number of links:",eu(bits))

