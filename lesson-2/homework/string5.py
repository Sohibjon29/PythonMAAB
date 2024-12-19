inp=input("Write a word\n")
vw=0
cns=0
vow=['a', 'e', 'o', 'u','i', 'y']
for char in inp:
    if char in vow:
        vw=vw+1
    else:
        cns=cns+1
print("There are", vw, "vowels and", cns, "consonants")
