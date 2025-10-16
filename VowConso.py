t=input()
v=0
c=0
for i in t:
    if i in 'aeiouAEIOU':
        v+=1
    elif i.isalpha():
        c+=1
print("Vowels:",v)
print("Consonants:",c)