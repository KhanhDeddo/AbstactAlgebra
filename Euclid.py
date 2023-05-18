#Thuat toan Euclide.
def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

def control():
    print("Tim ucln(a,b)")
    a=int(input("a = "))
    b=int(input("b = "))
    print(f"UCLN({a},{b}) là: {GCD(a,b)}")
control()