# Code from Primo
def ist_prim(n): 
    return n > 1 and all(n % i for i in range (2, int(n**0.5)+1))

PrimoLoop = True

while PrimoLoop:
    try: 
        zahl =  int(input('Enter number: '))
    except: continue
    print("It is a Primenumber." if ist_prim(zahl) else "is not a prim number.")
