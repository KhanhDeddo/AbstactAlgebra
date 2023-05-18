def euclidExtended(a,b):
    count=0
    if a<b:
        count+=1
        a,b=b,a
    d,r=a,b
    y0,y1,n=0,1,1
    while r!=0:
        y2=((d//r)*y1+y0)
        d,r,y0,y1=r,d%r,y1,y2
        n+=1
    y=y0*(-1)**n
    x=(d-y*b)//a
    if count:
        x,y=y,x
    return d,x,y

def control():
    print("Tim x,y,ucln(a,b) thoa man ax + by = ucln(a,b)")
    a=int(input("a = "))
    b=int(input("b = "))
    d,x,y=euclidExtended(a,b)
    print("\nKet qua:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"ucln({a},{b}) là: {d}")
    print(f"{a}x{x} + {b}x{y} = {d}")
control()