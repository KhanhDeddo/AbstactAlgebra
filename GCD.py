def GCD(a,b):
    if b==0:
        return a
    print(a,b,a%b)
    return GCD(b,a%b)
print(GCD(360,924))