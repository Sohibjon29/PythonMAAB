inp=input("Write anything \n")
lng=int(len(inp))
for i in inp:
    if inp.rfind(i)!=int(inp[lng-i-1]):
        print("It is not palindrome")
    else: 
        if inp.rfind(i)==lng-1:
            print("it is palindrome")

