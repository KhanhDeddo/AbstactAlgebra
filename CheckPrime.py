#Kiem Tra 1 so có phai là so nguyen to hay khong.
import os
from IPython.display import clear_output

def checkPrimeNumber(n):
    if n==2 or n==3:
        return True
    elif n<2 or n%2==0 or n%3==0:
        return False
    else:
        i=5
        while i**2<=n:
            if n%(i)==0 or n%(i+2)==0:
                return False
            i+=6
    return True

def Control():
    while True:
        os.system("clr")
        clear_output()
        print("Kiem Tra 1 so có phai la so nguyen to hay khong.")
        n=int(input("Nhap mot so nguyen bat ki: "))
        print(checkPrimeNumber(n))
        print("\nDong chuong trinh nhap:-1")
        control=input("Tiep tuc an Enter.")
        if control=="-1":     
            os.system("clr")
            clear_output()
            print("Chuong trinh da dong.")
            break
Control()