l="abcdefghijklmnopqrstuvwxyz"
alpha= list(map(lambda x: x, l))

en=dict()
en[" "]="$"
s,l=0,len(alpha)-1



while s<len(alpha):
    
    en[alpha[s]]=alpha[l]
    s+=1
    l-=1
    
data=input("Enter the message to encrypt: ")
data=data.lower()

for i in data:
    d=en[i]
    print(d,end="")
