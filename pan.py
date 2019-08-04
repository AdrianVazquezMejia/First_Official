#Adrian_Vazquez
#11\02\2019
#Pandigital_Step_Number
#Made : 02/12/2019
#Country: Venezuela
#email: aavm0000@gmail.compile

#Hi, I want so say thank you, I learnt a lot with this challenge, I follow your page and all your projects.
#At firts place I generate a sequence of step.numbers from 989898989 up to 101.010.101.010.101.010.101, and
#I verify if someone is pandigital and count it.
#The sequence was generate based on a patern that i identified, adding and substracting numbers from each digit
#that compose that number.
#For example (3210) for all number until but no including the last one I add 2 to the last one and then
#to the next (3212,3232) the sequece is (+2,-0,-2,-4,.....) for especial cases repeat the number of the sequece
#for the last number (+1,-1,-3,-6,.....)
#To add a new digit (+1,-9,-8,-9,......)
#I did it based on list, So i didn't use so much memory.

#It takes about 10 minuts to retrieve the result



#Thank you 

#PD: I live in venezuela, and I´m living a really hard situation (If you want to verify just comunicate with me), 
#I almost dont have money to buy food, I study in a difficult way,
#I have a mini laptop, 1 GB RAM, Intel inside, 9'',  
#If I win, I will buy a better computer and I will donate this to someone else.
#You will verify all the process
#All this in order to keep  advancing in this science,
# and to help to my comunity in the access to the tech and coding


#Thank you again , paypal is the same as my email.
#thank you. 

n=list('989898989')
cantidad=0

h=0
def is_x_in_n(n,x):
    n=n[:]
    l=len(n)
    found=False
    for i in range(l):
        if x==int(n[i]):
            found=True
    return found
def pandigital(n):
    l=len(n)
    pan=False
    for i in range(10):
        pan=is_x_in_n(n,i)
        if pan==False:
            break
    return pan

def longitud(n):
    n=n[:]
    l=len(n)
    i=whre(n)
    bol=0
    s=str(int(n[l-i-1])+2)
    #print(s)
    if len(s)>1:
        bol=1
    return bol

def lastone(n):
    n=n[:]
    l=len(n)
    k=1
    n[0]=str(int(n[0])+1)
    for i in range(1,l):
        naux=int(n[i])-k
        excede=int(n[i-1])-naux
        if naux<0 or (excede>1):
            k=k-2
            naux=int(n[i])-k
            if naux<0:
                naux=-naux
        n[i]=str(naux)
        #print(n[i])
        k=k+2
        
    return n
def whre(n):
    n=n[:]
    l=len(n)
    r=range(0,l)
    for i in r:
        if ((n[l-i-1] < n[l-i-2]) and (n[l-i-2]!='9')):
            break

    
    return i	
def nextstep(n):
    n=n[:]
    l=len(n)
    i=whre(n)
    n[l-i-1]=str(int(n[l-i-1])+2)
    j=0
    k=0
    while j!=i :
        naux=int(n[l-i+j])-k
        if naux<0:
            k=k-2
            naux=int(n[l-i+j])-k		
        n[l-i+j]=str(naux)
        j=j+1
        k=k+2
    return n



def inc_len(n):
    a=['1']
    l=len(n)
    k=True
    for i in range(l):
        if (k==True):
            n[i]=str(int(n[i])-9)
            k=False			
        else:
            n[i]=str(int(n[i])-7)
            k=True
    n=a+n
    return n

	
l=len(n)
while(l<21):
    l=len(n)
    j=whre(n)
    
    if (j==l-1) or (longitud(n)==1):
        naux=lastone(n)

        add=len(naux[0])
        if add>1:
            n=inc_len(n)
        else:
            n=naux
    else:
       n=nextstep(n)
    if pandigital(n)==True:
        cantidad=cantidad+1

print(cantidad)
