import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER='0123456789'
symbols="(){}[];:/"

all = lower +upper + NUMBER

length=16
password="".join(random.sample(all,length))


print(password)
