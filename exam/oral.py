def is_prime(num):
    i=2
    while i<num:
        if num%i==0:
            print(True)
        i+=1
is_prime(2)