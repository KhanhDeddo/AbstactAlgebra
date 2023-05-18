#TIM NGICH DAO BANG EUCLIDE MO RONG.
#thuat toan euclid mo rong.
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
#ham tra ve kq.
def inverse(a,m):
    d,x,y=euclidExtended(a,m)
    if d==1:
        print(f"Nghich dao cua {a} theo modulo {m} la: {x%m}\n")
    else:
        print(f"{a} khong co kha nghich theo modulo {m}. Vi UCLN({a},{m}) = {gcd(a,m)} != 1\n")


#TIM NGICH DAO BANG EULER.
#thuat toan euclid.
def gcd(a,m):
    if m==0:
        return a
    return gcd(m,a%m)
#danh sach so nguyen to la uoc cua m
def primeFactorization(m):
    lis=[]
    for i in range(2,m+1):
        count=0
        while m%i==0:
            count+=1
            m//=i
        if count:
            lis.append(i)
    return lis

#Nghich dao cua a.
def inverseOfA(a,m,lis):
    s=m
    for i in lis:#Tinh phi(m).
        s=s*(1-(1/i))
    return f"{a}^{int(s-1)}"

#Nhi phan (phi(m)-1)
def binary(b):
    lis=list(map(int,b.split("^")))#Tach lay so mu.
    base2=""
    while((lis[1])>0):
        base2+=str(lis[1]%2)
        lis[1]//=2
    return base2

#Chuyen phi(m)-1 tu nhi phan ve dang cơ số 2: phi(m)-1=2^z+2^k+...
def change(base2):
    lis=[]
    for i in range(len(base2)-1,-1,-1):
        if base2[i]=="1":
            lis=[i]+lis # chèn số mu cua 2 vào đầu danh sách.
    return lis

#ham tra ve kq.
def compact(a,m,lst,result,n=0):
    if n in lst:
        result*=a
    if n==lst[-1]:
        return result%m
    return compact(a**2%m,m,lst,result,n+1)

def control():
    print("Tim nghich dao cua a theo modulo m. ")
    print("1. Phuong Phap Euclid mo rong.")
    print("2. Phuong Phap Euler.")
    while True:
        select=int(input("Chon phuong phap tim kiem hoac an 0 de shutdow: "))
        if select==0:
                print("Chuong trinh da dong.")
                break
        if select==1:
            a=int(eval(input("a = ")))
            m=int(eval(input("m = ")))
            inverse(a,m)
        elif select==2:       
            a=int(eval(input("a = ")))
            m=int(eval(input("m = ")))
            if gcd(a,m)==1:
                result=1 #Bien de lu nghich dao cua a khi da rut gon.
                lis=primeFactorization(m)#danh sach so nguyen to la uoc cua m
                b=inverseOfA(a,m,lis)#Nghich dao cua a.
                base2=binary(b)#Nhi phan (phi(m)-1),so mu cua b.
                lst=change(base2)#Chuyen so mu cua b tu nhi phan ve dang cơ số 2, sau do tra ve danh sach so mu cua 2.
                print(f"Nghich dao cua {a} theo modulo {m} la: {compact(a,m,lst,result)}\n")
            else:
                print(f"{a} khong co kha nghich theo modulo {m}. Vi UCLN({a},{m}) = {gcd(a,m)} != 1\n")
            
control()