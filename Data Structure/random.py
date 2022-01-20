import random 
#print(random.randint(5,50))
#a=[5,3,1,9,0]
#print(random.choice(a))
a='1234567890asdfghjklqwertyuiopzxcvbnm!@#$%^&*()'
l=6
print("".join(random.sample(a,l)))