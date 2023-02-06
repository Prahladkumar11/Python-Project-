l="abcdefghijklmnopqrstuvwxyz"
l2=l[::-1]
alpha= list(map(lambda x: x, l2))
en=dict()
en["$"]=" "
s,l=0,len(alpha)-1



while s<len(alpha):
    
    en[alpha[s]]=alpha[l]
    s+=1
    l-=1
    
    
data=input("Enter the message to decrypt: ")
data=data.lower()

for i in data:
    d=en[i]
    print(d,end="")
